from functools import reduce


def extended_gcd_r(a, b):
    if b == 0:
        return a, 1, 0

    d, x, y = extended_gcd_r(b, a % b)
    return d, y, x - y * (a // b)


def modinv(a, m):
    g, x, y = extended_gcd_r(a, m)
    if g != 1:
        raise ValueError

    return x % m


def crt(a, m):
    M = reduce(lambda x, y: x * y, m)

    M_ = [M // mi for mi in m]

    N = [modinv(Mi, mi) for Mi, mi in zip(M_, m)]

    res = sum([ai * Ni * Mi for ai, Mi, Ni in zip(a, N, M_)])

    return res % M
