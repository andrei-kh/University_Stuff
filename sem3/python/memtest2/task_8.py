d = {}

out = open('output.txt', 'w')
with open('input.txt') as f:
    for line in f.readlines():
        for word in line.split():
            d[word] = d.get(word, 0) + 1

d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

for i in range(len(d) - 1):
    print(d[i][0], file=out)
print(d[-1][0], end='', file=out)
