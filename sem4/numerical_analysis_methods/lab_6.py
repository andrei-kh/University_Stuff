# Variant 24
from util import plotfunc, print_table
from sympy.abc import x
from sympy import lambdify
import matplotlib.pyplot as plt

points = [
    (0.68, 0.80866),
    (0.73, 0.89492),
    (0.80, 1.022964),
    (0.88, 1.20966),
    (0.93, 1.34087),
    (0.99, 1.52368)
]

in_point = 0.955

def lagrange_interpolation(points):
    Lequ = 0
    for i in range(len(points)):
        part = 1
        for j in range(len(points)):
            if i != j:
                part *= (x - points[j][0]) / (points[i][0] - points[j][0])
        part *= points[i][1]

        Lequ += part

    return Lequ


def eitken_formula(points):
    def Pcompute(i, j, n, p):
        if j - i == 1:
            return 1 / (p[j][0] - p[i][0]) * ((x - p[i][0]) * p[j][1] - (x - p[j][0]) * p[i][1])

        return 1 / (p[j][0] - p[i][0]) * (
            (x - p[i][0]) * Pcompute(i + 1, j, n, p) - (x - p[j][0]) * Pcompute(i, j - 1, n, p))

    return Pcompute(0, len(points) - 1, len(points) - 1, points)


Lequ = lagrange_interpolation(points)
L = lambdify([x], Lequ)

Pequ = eitken_formula(points)
P = lambdify([x], Pequ)

eres = []
for p in points:
    eres.append([p[0], p[1], P(p[0])])
print_table(eres, ['x', 'y', 'P(x)'], '.5f')
print()

print('Значение в точке x = {} по многочлену Лагранжа: {}'.format(in_point, format(L(in_point), '.7f')))
print('Значение в точке x = {} по     формуле Эйткена: {}'.format(in_point, format(P(in_point), '.7f')))

fig, ax = plt.subplots()
ax.set_title("Многочлен Лагранжа")
plt.scatter([p[0] for p in points], [p[1] for p in points], color='r')
plotfunc(L, -2, 2, 20000, figAx=(fig, ax))

fig, ax = plt.subplots()
ax.set_title("Формула Эйткена")
plt.scatter([p[0] for p in points], [p[1] for p in points], color='r')
plotfunc(P, -2, 2, 20000, figAx=(fig, ax))
