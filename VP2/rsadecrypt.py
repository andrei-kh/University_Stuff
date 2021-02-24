from math import sqrt


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
        raise ValueError
    else:
        return x % m

def is_prime(a):
    for i in range(2, int(sqrt(a) + 1)):
        if a % i == 0:
            return False
    return True


n = int(input())
e = int(input())
c = int(input())

for i in range(2, int(sqrt(n) + 1)):
    if n % i == 0:
        if is_prime(i):
            p, q = i, n // i

fn = (p - 1) * (q - 1)
d = modinv(e, fn)
print(pow(c, d, n))
