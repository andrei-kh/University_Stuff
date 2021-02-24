out = open('output.txt', 'w')
with open('input.txt') as f:
    lines = f.readlines()[::-1]
    for i in range(len(lines) - 1):
        print(lines[i].strip(), file=out)
    print(lines[-1].strip(), end='', file=out)
