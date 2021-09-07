def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * \
        (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return('нет')
    else:
        return x % m

k1 = int(input())
k2 = int(input())
cipher = input()
res = ""
for c in cipher:
    res += chr(((ord(c) - ord('A')) * modinv(k2, 26) - k1) % 26 + ord('A'))

print(res)
