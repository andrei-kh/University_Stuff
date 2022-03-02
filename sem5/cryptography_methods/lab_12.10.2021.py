def extended_gcd_nr(a, b):
    x, y = 1, 0
    x1, y1 = 0, 1
    while b:
        q = a // b
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        a, b = b, a - q * b

    return a, x, y


def extended_gcd_r(a, b):
    if b == 0:
        return a, 1, 0

    d, x, y = extended_gcd_r(b, a % b)
    return d, y, x - y * (a // b)

def extended_gcd(a, b):
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    q = a0 // b0
    r = a0 - q * b0
    while r > 0:
        temp = t0 - q * t
        t0 = t
        t = temp
        temp = s0 - q * s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = a0 // b0
        r = a0 - q * b0
    r = b0

    return r, s, t
