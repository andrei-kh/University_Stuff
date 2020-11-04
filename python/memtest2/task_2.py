out = open('output.txt', 'w')
with open('input.txt') as f:
    for line in f.readlines()[::-1]:
        print(line[::-1], end='', file=out)
