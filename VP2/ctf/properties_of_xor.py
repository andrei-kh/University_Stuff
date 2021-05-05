flag_xor = "646b720f0b3b191646405929766b4d605c485e785f713d171e02"
key2_key3 = "5f565957193f535c451e5e0f111c45625f09581c02391d070019"
key1 = "584f5228666b3132332c584f52286b32332c6b31292974796866"

s1 = bytearray.fromhex(flag_xor)
s2 = bytearray.fromhex(key2_key3)
s3 = bytearray.fromhex(key1)

res = [chr(a ^ b ^ c) for a, b, c in zip(s1, s2, s3)]
print("".join(res))
