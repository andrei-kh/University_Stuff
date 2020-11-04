inp = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = ''
for c in inp:
    if c.isalpha():
        res += alphabet[(alphabet.index(c) + 13) % len(alphabet)]
    else:
        res += c

print(res)
