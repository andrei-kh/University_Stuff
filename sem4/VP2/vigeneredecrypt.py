k = input().strip()
m = input().strip()

res = ''
for i in range(len(m)):
    res += chr((ord(m[i]) - ord(k[i % len(k)])) % 26 + ord('A'))

print(res)