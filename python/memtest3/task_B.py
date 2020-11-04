alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

key = ['C', 'A', 'B', 'F', 'D', 'E', 'I', 'G', 'H', 'L', 'J', 'K', 'O',
       'M', 'N', 'R', 'P', 'Q', 'U', 'S', 'T', 'X', 'V', 'W', 'Z', 'Y']

inp = input()
res = ''

for c in inp:
    if c.isalpha():
        c = key[alphabet.index(c)]
    res += c

print(res)
