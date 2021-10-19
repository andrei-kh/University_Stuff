import matplotlib.pyplot as plt
import math
from sympy import parse_expr, lambdify


"""
Вариант 24
u'' + p * u' + q * u = f
u'' - 2 * u' + 1 * u = 2e^x / (x + 1) ^ 3
u(0) = 1
u'(1) = e / 4
u(x) = e ^ x / (x + 1)
"""


def task(a=0, b=1, alpha0=1, alpha1=0, beta0=0, beta1=1, A=1, B=math.e / 4,
         p=parse_expr("-2"),
         q=parse_expr("1"),
         f=parse_expr("(2 * exp(x)) / ((x + 1) ** 3)"),
         u=parse_expr("exp(x) / (x + 1)"),
         h=0.1,
         ):

    n = int((b - a) / h)
    x = [a + h * i for i in range(n + 1)]

    lams = {v: lambdify(list(v.free_symbols), v) for v in [p, q, f, u]}
    p, q, f, u = map(lambda func: get_values(x, lams, func), (p, q, f, u))

    matrix = make_tridiagonal_matrix(p, q, f, n, A, B, alpha0, alpha1, beta0, beta1, h)

    y = tridiagonal_matrix_algo(*matrix)

    plt.plot(x, y, label='приближенное решение')
    plt.plot(x, u, label='точное решение')
    plt.legend()
    plt.show()


def tridiagonal_matrix_algo(a_, b_, c_, d_):
    a, b, c, d = map(lambda x: x.copy(), (a_, b_, c_, d_))
    n = len(d)
    for i in range(1, n):
        m = a[i - 1] / b[i - 1]
        b[i] = b[i] - m * c[i - 1]
        d[i] = d[i] - m * d[i - 1]

    y = b
    y[-1] = d[-1] / b[-1]

    for i in range(n - 2, -1, -1):
        y[i] = (d[i] - c[i] * y[i + 1]) / b[i]

    return y


def get_values(x, lams, f):
    return [lams[f](x[i]) if f.free_symbols else lams[f]() for i in range(len(x))]


def make_tridiagonal_matrix(p, q, f, n, A, B, alpha0, alpha1, beta0, beta1, h):
    # y0 *(h * alpha0 - alpha1) + alpha1 * y1 = A * h
    a, b, c, d = [], [h * alpha0 - alpha1], [alpha1], [A * h]

    for i in range(n - 1):
        a.append((2 - h * p[i]))
        b.append(2 * h * h * q[i] - 4)
        c.append(2 + h * p[i])
        d.append(2 * h * h * f[i])

    # yn * (h * beta0 + beta1) - beta1 * yn-1 = B * h
    a.append(-beta1)
    b.append(h * beta0 + beta1)
    d.append(B * h)

    return a, b, c, d


if __name__ == '__main__':
    task()
