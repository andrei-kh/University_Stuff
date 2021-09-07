import base64

string = "72bca9b68fcece17ac864a2cb6bfb6dbea1f7e271edb6dbf"

string_bytes = bytearray.fromhex(string)

res = base64.b64encode(string_bytes)

res = res.decode('ascii')

print(res)
