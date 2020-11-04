out = open('output.txt', 'w')
max = -1
max_str = ''
with open('input.txt') as f:
    for line in f.readlines():
        for word in line.split():
            if(len(word) > max):
                max = len(word)
                max_str = word

print(max_str, end='', file=out)
