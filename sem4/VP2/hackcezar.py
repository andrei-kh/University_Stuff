cipher = input()

d = {}
for c in cipher:
    d[c] = d.get(c, 0) + 1

count = len(cipher)
for key in d:
    d[key] = d[key] / count

d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
letter = list(d.keys())[-1]
print(ord(letter) - ord('E'))
