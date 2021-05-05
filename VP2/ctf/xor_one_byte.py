data = [5, 20, 31, 22, 18, 9, 29, 17, 9, 17, 57, 21, 9, 57, 85, 7, 21, 31, 57, 18, 9, 57, 21, 86, 10, 16, 85, 27]

key = ord('{') ^ data[6]

for i in range(0, len(data)):
    data[i] = chr(data[i] ^ key)

if data[6] == '{':
    print("".join(data))
