from typing import List, Tuple
from random import choice
from math import gcd


def find_all_coprimes_in_range(start: int, finish: int, number: int) -> List[int]:
    return [i for i in range(start, finish + 1) if gcd(number, i) == 1]


def extended_gcd_with_traceback(a: int, b: int) -> Tuple[int, int, int]:
    traceback = []
    x, y = 1, 0
    x1, y1 = 0, 1
    while b:
        q = a // b
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        traceback.append((a, b, q, a % b))
        a, b = b, a - q * b
    return a, x, y, traceback


def visualize_extended_gcd_traceback(traceback):
    for a, b, q, r in traceback[::-1][1:]:
        print(f"\t{r} = {a} - {q} * {b}")


def visualized_inverse(p, a):
    res, x, y, traceback = extended_gcd_with_traceback(p, a)
    print(f"Обратное число {a}: {y % p}")
    visualize_extended_gcd_traceback(traceback)
    print(f"\t{res} = {a} * {y} + {p} * {x} => {a} * {y % p} = {res} (mod {p})")
    return y % p


def get_a_and_b(p):
    coprimes = find_all_coprimes_in_range(1, p - 2, p - 1)
    a = choice(coprimes)
    while True:
        b = choice(coprimes)
        if a != b:
            return a, b


def gcd_with_traceback(a, b):
    traceback = []
    while b != 0:
        traceback.append((a, b, a // b, a % b))
        a, b = b, a % b
    return a, traceback


def visualize_gcd_traceback(traceback):
    for a, b, q, r in traceback:
        print(f"\t{a} = {q} * {b} + {r}")


def visualized_gcd(a, b):
    res, traceback = gcd_with_traceback(a, b)
    print(f"НОД({a}, {b}) = {res}")
    visualize_gcd_traceback(traceback)


def visual_binary_pow(a, b, mod):
    bin_ = bin(b)[2:]
    print(f"bin({b}) = `{bin_}`")
    print(f"a_0 = {a}")
    print("a_i = a_{i - 1} ^ 2 * a ^ d_i")
    a_i = a
    for i in range(1, len(bin_)):
        print(f"a_{i} = {a_i} ^ 2 * {a} ^ {int(bin_[i])} = "
              f"{a_i ** 2} * {a ** int(bin_[i])} = {(a_i ** 2) % mod} * {(a ** int(bin_[i]))} = "
              f"{((a_i ** 2) * (a ** int(bin_[i]))) % mod}")
        a_i = ((a_i ** 2) * (a ** int(bin_[i]))) % mod
    return (a ** b) % mod


def do_task(p, m, a=None, b=None):
    if a is None or b is None:
        a, b = get_a_and_b(p)
    print(f"Число а: {a}")
    visualized_gcd(p - 1, a)
    print(f"Число b: {b}")
    visualized_gcd(p - 1, b)
    print("\n-------\n")

    alpha = visualized_inverse(p - 1, a)
    beta = visualized_inverse(p - 1, b)
    print("\n-------\n")

    print("m_1 = m ^ a (mod p)")
    m = visual_binary_pow(m, a, p)
    print(f"m_1 = {m}\n")
    print("m_2 = m_1 ^ b (mod p)")
    m = visual_binary_pow(m, b, p)
    print(f"m_2 = {m}\n")
    print("m_3 = m_2 ^ alpha (mod p)")
    m = visual_binary_pow(m, alpha, p)
    print(f"m_3 = {m}\n")
    print("m_4 = m_3 ^ beta (mod p)")
    m = visual_binary_pow(m, beta, p)
    print(f"m_4 = {m}\n")
    print("Done...")


def do_task_open(p1, p2, q1, q2, m, a=None, b=None):
    ra = p1 * p2
    phi_ra = (p1 - 1) * (p2 - 1)
    rb = q1 * q2
    phi_rb = (q1 - 1) * (q2 - 1)
    if a is None:
        a, _ = get_a_and_b(phi_ra)
    if b is None:
        b, _ = get_a_and_b(phi_rb)
    alpha = visualized_inverse(phi_ra, a)
    beta = visualized_inverse(phi_rb, b)
    print("m_1 = m ^ b (mod r_b)")
    m = visual_binary_pow(m, b, rb)
    print(f"m_1 = {m}\n")
    print("m_2 = m_1 ^ beta (mod r_b)")
    m = visual_binary_pow(m, beta, rb)
    print(f"m_2 = {m}\n")
    print("done")


def do_task_podpis(p1, p2, q1, q2, m, a=None, b=None):
    ra = p1 * p2
    phi_ra = (p1 - 1) * (p2 - 1)
    rb = q1 * q2
    phi_rb = (q1 - 1) * (q2 - 1)
    if a is None:
        a, _ = get_a_and_b(phi_ra)
    if b is None:
        b, _ = get_a_and_b(phi_rb)
    alpha = visualized_inverse(phi_ra, a)
    beta = visualized_inverse(phi_rb, b)
    print("m_1 = m ^ beta (mod r_b)")
    m = visual_binary_pow(m, beta, rb)
    print(f"m_1 = {m}\n")
    print("m_2 = m_1 ^ a (mod r_a)")
    m = visual_binary_pow(m, a, ra)
    print(f"m_2 = {m}\n")
    print("m_3 = m_2 ^ alpha (mod r_a)")
    m = visual_binary_pow(m, alpha, ra)
    print(f"m_3 = {m}\n")
    print("m_4 = m_3 ^ b (mod r_b)")
    m = visual_binary_pow(m, b, rb)
    print(f"m_4 = {m}\n")
    print("done")


if __name__ == "__main__":
    do_task(23, 17, 3, 5)
    # do_task_open(7, 23, 5, 11, 40)
    # do_task_podpis(7, 23, 5, 11, 40)
