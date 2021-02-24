letters = 0
words = 0
lines = 0
out = open('output.txt', 'w')
with open('input.txt') as f:
    word = ''
    while True:
        c = f.read(1)
        if not c:
            break
        if c == '\n':
            lines += 1
        if c.isalpha():
            letters += 1
            word += c
        elif word != '':
            word = ''
            words += 1

print('Input file contains:', file=out)
print(letters, 'letters', file=out)
print(words, 'words', file=out)
print(lines, 'lines', file=out)
