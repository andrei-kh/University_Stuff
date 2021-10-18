import matplotlib.pyplot as plt
import math
from sympy import Symbol, solve, parse_expr, lambdify


"""
Вариант 24
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
    p = [lams[p](x[i]) if p.free_symbols else lams[p]() for i in range(n + 1)]
    q = [lams[q](x[i]) if q.free_symbols else lams[q]() for i in range(n + 1)]
    f = [lams[f](x[i]) if f.free_symbols else lams[f]() for i in range(n + 1)]
    u = [lams[u](x[i]) if u.free_symbols else lams[u]() for i in range(n + 1)]

    system, yi = [], [Symbol('y0'), Symbol('y1')]

    for i in range(n - 1):
        yi.append(Symbol(f'y{i + 2}'))
        system.append(
            (2 - h * p[i]) * yi[i] + (2 * h * h * q[i] - 4) * yi[i + 1] + (2 + h * p[i]) * yi[i + 2] - 2 * h * h * f[i]
        )
    system.append(alpha0 * yi[0] + alpha1 * (yi[1] - yi[0]) / h - A)
    system.append(beta0 * yi[n] + beta1 * (yi[n] - yi[n - 1]) / h - B)

    y = solve(system, *yi).values()
    plt.plot(x, y, label='приближенное решение')
    plt.plot(x, u, label='точное решение')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    task()
