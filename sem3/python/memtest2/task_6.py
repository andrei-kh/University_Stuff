res = 0

out = open('output.txt', 'w')
with open('input.txt') as f:
    for line in f.readlines():
        res += len(line.split())

print(res, end='', file=out)
