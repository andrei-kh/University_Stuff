import argparse
import sys

from base64 import b64decode, b64encode
from typing import Any, Tuple

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util import Padding

KEY_PROTECTION = "scryptAndAES128-CBC"


class CryptoHandler:
    def __init__(self, private_key="private.pem", public_key="public.pem",
                 protection=None, session_key_len=16, bits=2048) -> None:
        self.private_key_path = private_key
        self.public_key_path = public_key
        self.protection = protection
        self.session_key_len = session_key_len
        self.bits = bits

    def encrypt_file_to_file(self, file_path: str, output_path: str) -> None:
        encrypted_string = self.encrypt_file_to_bytes(file_path)
        self.write_bytes_to_file(encrypted_string, output_path)

    def decrypt_file_to_file(self, file_path: str, output_path: str) -> None:
        decrypted_string = self.decrypt_file_to_string(file_path)
        self.write_str_to_file(decrypted_string, output_path)

    def encrypt_file_to_bytes(self, file_path: str) -> bytes:
        string = self.read_str_from_file(file_path)
        return self.encrypt_string(string)

    def decrypt_file_to_string(self, file_path: str) -> str:
        string = self.read_bytes_from_file(file_path)
        return self.decrypt_string(string)

    def encrypt_string(self, string: str) -> bytes:
        session_key, ciphertext = self.encrypt_aes(string)
        enc_session_key = self.encrypt_bytes_rsa(session_key)

        return b64encode(enc_session_key + ciphertext)

    def encrypt_bytes_rsa(self, bytes_: bytes) -> bytes:
        public_key = self.read_public_key()
        cipher_rsa = PKCS1_OAEP.new(public_key)
        return cipher_rsa.encrypt(bytes_)

    def encrypt_aes(self, string: str) -> Tuple[bytes, bytes]:
        session_key = get_random_bytes(self.session_key_len)
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(string.encode())

        return session_key, cipher_aes.nonce + tag + ciphertext

    def decrypt_string(self, string: bytes) -> str:
        private_key_len = self.get_private_key_len()
        enc_session_key, nonce, tag, ciphertext = self.prepare_encrypted_bytes(string, private_key_len)
        session_key = self.decrypt_bytes_rsa(enc_session_key)

        return self.decrypt_aes(session_key, nonce, tag, ciphertext)

    def decrypt_bytes_rsa(self, bytes_: bytes) -> bytes:
        private_key = self.read_private_key()
        cipher_rsa = PKCS1_OAEP.new(private_key)

        return cipher_rsa.decrypt(bytes_)

    def decrypt_aes(self, session_key: bytes, nonce: bytes, tag: bytes, ciphertext: bytes) -> str:
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)

        return plaintext.decode()

    def prepare_encrypted_bytes(self, bytes_: bytes, private_key_len: int) -> Tuple[bytes, bytes, bytes, bytes]:
        encrypted_bytes = b64decode(bytes_)

        enc_session_key, encrypted_bytes = self.split_string_at(encrypted_bytes, private_key_len)
        nonce, encrypted_bytes = self.split_string_at(encrypted_bytes, self.session_key_len)
        tag, ciphertext = self.split_string_at(encrypted_bytes, self.session_key_len)

        return enc_session_key, nonce, tag, ciphertext

    def get_private_key_len(self) -> int:
        return self.read_private_key().size_in_bytes()

    def generate_and_save_keys(self) -> None:
        keys = self.generate_key(self.bits)
        self.write_keys(keys)

    def generate_key(self, bits: int = 2048) -> RSA.RsaKey:
        key = RSA.generate(bits)

        return key

    def read_private_key(self) -> RSA.RsaKey:
        private_key = self.read_bytes_from_file(self.private_key_path)
        return RSA.import_key(private_key, passphrase=self.protection)

    def read_public_key(self) -> RSA.RsaKey:
        public_key = self.read_bytes_from_file(self.public_key_path)
        return RSA.import_key(public_key)

    def read_bytes_from_file(self, path: str) -> bytes:
        return self.read_file(path, "rb")

    def read_str_from_file(self, path: str) -> str:
        return self.read_file(path, "r")

    def read_file(self, path: str, mode: str) -> str:
        with open(path, mode) as file:
            return file.read()

    def write_keys(self, keys: RSA.RsaKey) -> None:
        self.write_private_key(keys)
        self.write_public_key(keys)

    def write_private_key(self, keys: RSA.RsaKey) -> None:
        encrypted_key = keys.export_key(passphrase=self.protection, pkcs=8,
                                        protection=KEY_PROTECTION)
        self.write_bytes_to_file(encrypted_key, self.private_key_path)

    def write_public_key(self, keys: RSA.RsaKey) -> None:
        public_key = keys.publickey().export_key()
        self.write_bytes_to_file(public_key, self.public_key_path)

    def write_bytes_to_file(self, bytes_: bytes, path: str) -> None:
        return self.write_file(path, "wb", bytes_)

    def write_str_to_file(self, string: str, path: str) -> None:
        return self.write_file(path, "w", string)

    def write_file(self, path: str, mode: str, content: Any) -> None:
        with open(path, mode) as file:
            file.write(content)

    def split_string_at(self, string: str, pos: int) -> tuple:
        return string[:pos], string[pos:]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("-e", "--encrypt", help="encrypt", action="store_true")
    action.add_argument("-d", "--decrypt", help="decrypt", action="store_true")

    inp = parser.add_mutually_exclusive_group(required=True)
    inp.add_argument("-str", "--string", help="String to encrypt or decrypt")
    inp.add_argument("-i", "--input", help="input file path")

    parser.add_argument("-g", "--generate", help="generate keys", action="store_true")
    parser.add_argument("-o", "--output", help="output file path")

    settings = parser.add_argument_group("settings")
    settings.add_argument("-public", "--public-key", help="key file path",
                          required="-private" in sys.argv or "--private-key" in sys.argv)
    settings.add_argument("-private", "--private-key", help="key file path",
                          required="-public" in sys.argv or "--public-key" in sys.argv)
    settings.add_argument("-p", "--protection", help="key protection")
    settings.add_argument("-b", "--bits", help="key length")
    settings.add_argument("-s", "--session-key-len", help="session key length (16, 24, 32)", type=int)
    args = parser.parse_args()

    settings_names = [action.dest for action in settings._group_actions]
    optional = {name: val for name, val in args._get_kwargs() if name not in settings_names}
    settings = {name: val for name, val in args._get_kwargs() if name in settings_names}

    optional["settings"] = argparse.Namespace(**settings)
    return argparse.Namespace(**optional)


def only_aes():
    session_key = get_random_bytes(32)
    iv = b"\x00" * AES.block_size

    aes = AES.new(session_key, AES.MODE_CBC, iv)

    text = "Cool encrypted tex".encode()
    text = Padding.pad(text, AES.block_size)

    enc = aes.encrypt(text)

    return b64encode(enc).decode(), bytes.hex(session_key)


if __name__ == '__main__':
    args = parse_args()

    settings = {key: val for key, val in vars(args.settings).items() if val is not None}

    cryptohandler = CryptoHandler(**settings)

    if args.generate:
        cryptohandler.generate_and_save_keys()

    if args.string:
        if args.encrypt:
            print(cryptohandler.encrypt_string(args.string).decode())
        elif args.decrypt:
            print(cryptohandler.decrypt_string(args.string))

    if args.input:
        if args.encrypt:
            if args.output:
                cryptohandler.encrypt_file_to_file(args.input, args.output)
            else:
                print(cryptohandler.encrypt_file_to_bytes(args.input).decode())
        elif args.decrypt:
            if args.output:
                cryptohandler.decrypt_file_to_file(args.input, args.output)
            else:
                print(cryptohandler.decrypt_file_to_string(args.input))
