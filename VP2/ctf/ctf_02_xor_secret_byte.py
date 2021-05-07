import re

string = "77666d64607b6f246c25214b26214b794d4b7220622461662523274b766d405169"

barr = bytearray.fromhex(string)

for i in range(256):
    res = "".join([chr(b ^ i) for b in barr])
    match = re.search(r"crypto{.*}", res)
    if match:
        print(match.group(0))
        break