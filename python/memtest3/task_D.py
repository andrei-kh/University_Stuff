inp = input()
n = int(input())
keys = []
for i in range(n):
    inp_ = input().split()
    keys.append((inp_[0], inp_[1]))

res = []
for num, key in keys:
    key_f = key * (len(inp) // len(key) + 1)
    coded = []
    for i in range(len(inp)):
        coded.append(ord(inp[i]) ^ ord(key_f[i]))

    res.append((num, len(coded) - len(set(coded))))

res = sorted(res, key=lambda x: (x[1]))
print(res[0][0])
