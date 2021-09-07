n = int(input())
cipher = input()

res = ''
for i in range(len(cipher) // n):
    for j in range(n):
        res += cipher[i + (len(cipher) // n) * j]

print(res)
