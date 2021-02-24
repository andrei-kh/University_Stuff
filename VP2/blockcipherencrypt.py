n = int(input())

table = []
for i in range(n):
    table.append(int(input()))

m = input()
if len(m) % n:
    m += (n - (len(m) % n)) * '_'

table *= (len(m) // n)
for i in range(n, len(table)):
    table[i] += (i // n) * n

res = [None for _ in range(len(m))]

for i in range(len(m)):
    res[table[i]] = m[i]

print("".join(res))
