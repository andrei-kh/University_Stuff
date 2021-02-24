from collections import defaultdict

d = defaultdict(int)

out = open('output.txt', 'w')
with open('input.txt') as f:
    for line in f.readlines():
        for word in line.split():
            print(d[word], end=' ', file=out)
            d[word] += 1
