n = int(input())

table = []
for i in range(n):
    table.append(int(input()))

m = input()

res = [None for _ in range(len(m))]

for i in range(len(m)):
    res[table[i]] = m[i]

print("".join(res))
