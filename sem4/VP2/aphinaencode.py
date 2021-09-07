k1 = int(input())
k2 = int(input())

cipher = input()
res = ''

for c in cipher:
    res += chr(int((ord(c) - ord('A') + k1) * k2) % 26 + ord('A'))

print(res)