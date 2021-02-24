import sympy  # pip install sympy


# Перевод в строку
def decode_mem(a):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    res = ''
    while a > 0:
        temp = a % 100
        if temp > len(alphabet):
            return None
        else:
            res += alphabet[temp - 1]
        a //= 100

    return res[::-1]


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


# инверсия ax mod m = 1
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    else:
        return x % m


# Расшифровка RSA
def decrypt_rsa(n, e, w):
    p, q = sympy.ntheory.factorint(n)
    f = (p - 1) * (q - 1)
    d = modinv(e, f)
    c = pow(w, d, mod=n)
    return c


def modular_sqrt(a, p):

    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


# Расшифровка Рабина
def decrypt_rabin(N, B, w):
    D = (B * B + 4 * w) % N
    p, q = sympy.factorint(N)
    crt = (D % p, D % q)
    rtp1 = modular_sqrt(crt[0], p)
    rtp2 = p - rtp1
    rtq1 = modular_sqrt(crt[1], q)
    rtq2 = q - rtq1
    pinv = modinv(p, q)
    d1 = (((rtq1 - rtp1) * pinv) % q) * p + rtp1
    d2 = (((rtq1 - rtp2) * pinv) % q) * p + rtp2
    d3 = (((rtq2 - rtp1) * pinv) % q) * p + rtp1
    d4 = (((rtq2 - rtp2) * pinv) % q) * p + rtp2
    twoinv = modinv(2, N)
    c1 = ((d1 - B) * twoinv) % N
    c2 = ((d2 - B) * twoinv) % N
    c3 = ((d3 - B) * twoinv) % N
    c4 = ((d4 - B) * twoinv) % N
    return (c1, c2, c3, c4)


# Расшифровка Эль Гамаля
def decode_el_gamal(P, g, h, w, Osk):
    x = -1
    base = g
    for i in range(2, P + 1):
        g = g * base
        if g == h:
            x = i
            break

    if x == -1:
        raise ValueError

    K = pow(Osk, x, mod=P)
    c = (w * modinv(K, P)) % P
    return c


rsa = [(33, 9, 20),
       (1147, 167, 691),
       (4144226923, 20449, 708173492),
       (4153748882242740779, 1299709, 3983064862319985375)]

rabin = [(697, 178, 425),
         (754499, 302, 517655),
         (8711962769, 452125232, 5000622672)]


gamal = [(1811, 6, 216, 1381, 1158),
         (507151027, 2, 324780822, 350245652, 161375365)]


for code in rsa:
    dec = decrypt_rsa(code[0], code[1], code[2])
    print(decode_mem(dec))
    print(dec)

for code in rabin:
    dec = decrypt_rabin(code[0], code[1], code[2])
    for c in dec:
        s = decode_mem(c)
        if s is not None:
            print(s)
    print(dec)

for code in gamal:
    dec = decode_el_gamal(code[0], code[1], code[2], code[3], code[4])
    print(decode_mem(dec))
    print(dec)
