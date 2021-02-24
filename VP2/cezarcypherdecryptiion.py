n = int(input())
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
# print(len(alph))
s = input().strip()
for c in s:
    print(alph[(ord(c) - ord('A') - n) % 26], end='')
