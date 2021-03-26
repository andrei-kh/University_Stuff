# Variant 24
from util import plotfunc
from sympy.abc import x
from sympy import lambdify
import matplotlib.pyplot as plt
from math import factorial
from sys import argv

points = [
    (0.0, 1.758),
    (0.8, 1.522),
    (1.6, 1.375),
    (2.4, 1.008),
    (3.2, 0.537),
    (4.0, 0.517),
    (4.8, 0.056),
    (5.6, 0.159),
    (6.4, -0.381),
    (7.2, -0.710),
    (8.0, -0.946),
    (8.8, -1.174),
    (9.6, -1.603),
    (10.4, - 1.837),
    (11.2, - 2.045),
    (12.0, - 2.211),
    (12.8, - 2.524),
    (13.6, - 2.599),
    (14.4, - 3.189),
    (15.2, - 3.280),
    (16.0, - 3.421),
]


def compute_finite_difference(points):
    deltas = [[p[1] for p in points]]

    while len(deltas[-1]) > 1:
        new_delta = []
        for i in range(0, len(deltas[-1]) - 1):
            new_delta.append(-deltas[-1][i] + deltas[-1][i + 1])

        deltas.append(new_delta)

    return deltas


def first_formula(points, n):
    h = points[1][0] - points[0][0]
    finite_diffs = compute_finite_difference(points)

    Pequ = 0
    for i in range(n + 1):
        part = 1
        for j in range(i):
            part *= ((x - points[0][0]) / h - j)
        Pequ += finite_diffs[i][0] * (part / factorial(i))

    P = lambdify([x], Pequ)

    return P


def second_formula(points, n):
    h = points[1][0] - points[0][0]
    finite_diffs = compute_finite_difference(points)

    Pequ = 0
    for i in range(n + 1):
        part = 1
        for j in range(i):
            part *= ((x - points[n][0]) / h + j)
        Pequ += finite_diffs[i][-1] * (part / factorial(i))

    return lambdify([x], Pequ)


P1 = first_formula(points, len(points) - 1)
res1 = []
for i in range(len(points)):
    res1.append([points[i][0], points[i][1], P1(points[i][0])])

fig, ax = plt.subplots()
ax.set_title("Первый многочлен")
plt.scatter([p[0] for p in points], [p[1] for p in points], color='r')
plotfunc(P1, -10, 10, 20000, figAx=(fig, ax))

if argv[-1] == 'check' or argv[-1] == 'check1':
    print("Проверка для 1го многочлена")
    while True:
        print("Input some x:", end=' ')
        inp = input()
        if inp == 'exit':
            break
        x_var = float(inp)
        print(P1(x_var))


P2 = second_formula(points, len(points) - 1)
res2 = []
for i in range(len(points)):
    res2.append([points[i][0], points[i][1], P2(points[i][0])])

fig, ax = plt.subplots()
ax.set_title("Второй многочлен")
plt.scatter([p[0] for p in points], [p[1] for p in points], color='r')
plotfunc(P2, -10, 10, 20000, figAx=(fig, ax))

if argv[-1] == 'check' or argv[-1] == 'check2':
    print("Проверка для 2го многочлена")
    while True:
        print("Input some x:", end=' ')
        inp = input()
        if inp == 'exit':
            break
        x_var = float(inp)
        print(P2(x_var))
