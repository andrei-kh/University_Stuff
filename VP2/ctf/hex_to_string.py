import re

string = "68656c6c6f2163727970746f7b596f755f77696c6c5f62655f776f726b696e675\
f776974685f6865785f737472696e67735f615f6c6f747d796573"

barr = bytearray.fromhex(string)

res = barr.decode()

print("full string:\n" + res)

key = re.search(r"crypto{.*}", res).group(0)

print("key:\n" + key)
