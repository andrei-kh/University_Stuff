from sympy.abc import x
from sympy import lambdify, Matrix
from util import plotfunc, print_table
import matplotlib.pyplot as plt

points = [
    [1.0, 1.8, 2.6, 3.4, 4.2, 5.0, 5.8, 6.6, 7.4, 8.2],
    [7.5, 5.3, 2.1, 1.01, 0.07, -1.1, -2.5, -4.8, -8.5, -12.2],
]


def compute_coeffs(p):
    a = [p[1].copy()]

    a.append([])
    a[1].append((p[1][1] - p[1][0]) / (p[0][1] - p[0][0]))
    for i in range(len(p[0]) - 1):
        a[1].append(2 * (p[1][i + 1] - p[1][i]) / (p[0][i + 1] - p[0][i]) - a[1][i])

    a.append([])
    for i in range(len(p[0]) - 1):
        a[2].append((a[1][i + 1] - a[1][i]) / (2 * (p[0][i + 1] - p[0][i])))
    a2n_1 = (p[1][len(p[0]) - 1] - p[1][len(p[0]) - 2]) / ((p[0][len(p[0]) - 1] - p[0][len(p[0]) - 2]) ** 2)
    a2n_1 -= a[1][len(p[0]) - 2] / ((p[0][len(p[0]) - 1] - p[0][len(p[0]) - 2]))
    a[2].append(a2n_1)

    return a


def spline_quadratic(p):
    S2 = []
    a = compute_coeffs(p)

    for i in range(len(p[0]) - 1):
        parab = a[0][i] + a[1][i] * (x - p[0][i]) + a[2][i] * ((x - p[0][i]) ** 2)
        S2.append(lambdify([x], parab))

    return S2


def spline_cubic(p):
    n = len(p[0])
    h = [p[0][i + 1] - p[0][i] for i in range(len(p[0]) - 1)]
    a = [y for y in p[1]]

    ma = [[0 for _ in range(n)] for __ in range(n)]
    ma[0][0] = 1
    for i in range(n - 1):
        if i != n - 2:
            ma[i + 1][i + 1] = 2 * (h[i] + h[i + 1])
        ma[i + 1][i] = h[i]
        ma[i][i + 1] = h[i]

    ma[0][1] = 0
    ma[n - 1][n - 2] = 0
    ma[n - 1][n - 1] = 1

    mb = [0]
    for i in range(n - 2):
        mb.append(3 * (a[i + 2] - a[i + 1]) / h[i + 1] - 3 * (a[i + 1] - a[i]) / h[i])
    mb.append(0)

    c = list(Matrix(ma).LUsolve(Matrix(mb)))

    S = []
    for i in range(n - 1):
        di = (c[i + 1] - c[i]) / (3 * h[i])
        bi = (a[i + 1] - a[i]) / h[i] - h[i] * (c[i + 1] + 2.0 * c[i]) / 3.0
        s = a[i] + bi * (x - p[0][i]) + c[i] * (x - p[0][i])**2 + di * (x - p[0][i])**3
        S.append(lambdify([x], s))

    return S


def handle_spline(S, p):
    table = []

    for i in range(len(p[0]) - 1):
        table.append(
            [i, S[i](p[0][i]), p[1][i], i + 1, S[i](p[0][i + 1]), p[1][i + 1]]
        )
    table.append([len(p[0]) - 1, S[-1](p[0][-1]), p[1][-1], '-', '-', '-'])
    print_table(table, ['i', 'Si(xi)', 'yi', 'i + 1', 'Si(xi+1)', 'yi+1'])
    print()

    fig, ax = plt.subplots()
    plt.scatter([p for p in p[0]], [p for p in p[1]], color='r')
    for i in range(len(p[0]) - 1):
        plotfunc(S[i], p[0][i], p[0][i + 1], 2000, figAx=(fig, ax), show=False)

    plotfunc(lambda x: None, p[0][1], p[0][-1], 1, xlim=(0, 10), ylim=(-13, 10), figAx=(fig, ax))


print("Квадратический сплайн")
S2 = spline_quadratic(points)
handle_spline(S2, points)

print("Кубический сплайн")
S3 = spline_cubic(points)
handle_spline(S3, points)
