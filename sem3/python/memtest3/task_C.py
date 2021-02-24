alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

inp = input()
res = ''
i = 1
while i < len(inp):
    if inp[i - 1] == ' ':
        res += ' '
        i += 1
    else:
        res += alphabet[(alphabet.index(inp[i]) - 1) % 26]
        i += 2

print(res)
