import math


def task_1():
    print(2**179)


def task_2():
    fact_20 = 1

    for i in range(2, 21):
        fact_20 *= i

    print(fact_20)


def task_3(a=179, b=971):
    print(math.sqrt(a ** 2 + b ** 2))


def task_4():
    print('A' * 100)


def task_5(a, b):
    print(a if a > b else b)


def task_6(a, b):
    print(1 if a > b else 2 if a < b else 0)


def task_7():
    print(int('179' * 50) ** 2)


def task_8(a, b):
    print(math.hypot(a, b))


def task_9(a, b, c):
    print(max(a, b, c))


def task_10(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('YES')
    else:
        print('NO')


def task_11(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        print('Yes')
    else:
        print('NO')


def task_12():
    print(int(str(179 ** 10) * 4) ** .1)


def task_13(a):
    print('YES' if (not(a % 4) and a % 100) or not(a % 400) else 'NO')


def task_14(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    print('YES' if dx == 1 and dy == 2 or dx == 2 and dy == 1 else 'NO')


def task_15(A, B):
    for i in range(A, B + 1):
        print(i, end=' ')


def task_16(n):
    print(n * (n + 1) * (2 * n + 1) / 6)


def task_17(n):
    print(math.factorial(n))


def task_18(n, k):
    if n >= k:
        print(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
    else:
        print('n must be greater or equal to k')


def task_19(n):
    penguine = ["   _~_    ",
                "  (o o)   ",
                r" /  V  \  ",
                r"/(  _  )\ ",
                "  ^^ ^^   "]

    if n < 1 or n > 9:
        print('Invalid n')
    else:
        for i in range(0, len(penguine)):
            print(penguine[i] * n)


def task_20(n, m, k):
    print('YES' if n * m > k and (not(k % n) or not(k % m)) else 'No')


def task_21(a, b):
    print('INF' if not(a) and not(b) else 'NO' if not(a) and b else -b / a)


def task_22():
    for i in range(100, 1000):
        if(i ** 2 % 1000 == i):
            print(i)


def task_23(n):
    if n > 9:
        print('Invalid n')
    else:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end='')
            print()


def task_24():
    a = int(input())
    b = int(input())
    c = int(input())

    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a

    print(a, b, c)


def task_25(n):
    sum = 0

    for i in range(1, n + 1):
        sum += math.factorial(i)

    print(sum)


task_25(10)
