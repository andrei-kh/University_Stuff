string_ = "eb213f2641e482b26217f27342e175d2e7a3c5b103e526217f27342e175de762634a1514"

barr = bytearray.fromhex(string_)
flag_start, flag_finish = "crypto{", "}"

key = [chr(a ^ ord(b)) for a, b in zip(barr, flag_start)]
print(key)

print([chr(a ^ ord(b)) for a, b in zip(barr, key * len(barr))])
