from collections import defaultdict

d = defaultdict(int)

out = open('output.txt', 'w')
with open('input.txt') as f:
    for line in f.readlines():
        for word in line.split():
            d[word] += 1

max_val = max(d.values())
max_keys = [k for k, v in d.items() if v == max_val]

print(min(max_keys), end='', file=out)
