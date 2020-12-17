import numpy as np
from sympy import Symbol
from sympy.solvers import solveset
from sympy import pprint
from sympy import init_printing
# from sympy import re

A = [
    [2, 1, 0],
    [1, 2, 1],
    [0, 8, 2]
]
a = np.array(A)
print('Матрица А:\n', a)

f = a
for i in range(f.shape[0] - 2, -1, -1):
    b = np.identity(f.shape[0])
    for j in range(f.shape[1]):
        if(i == j):
            b[i][j] = 1 / f[i + 1][i]
        else:
            b[i][j] = -f[i + 1][j] / f[i + 1][i]
    f = np.linalg.multi_dot([np.linalg.inv(b), f, b])
# Каноническая
print('\nМатрица Фробениуса\n', f)

p = f[0][:]
x = Symbol('x')
init_printing()
print('\nХарактеристическое уравнение:')
pprint(x**3 - p[0] * x ** 2 - p[1] * x - p[2])
Lambda = list(solveset(-x**3 + p[0] * x ** 2 + p[1] * x + p[2], x))

print('\nСобственные значения:')
print(*Lambda)

check = a.trace()
print('\nПроверка:')
print('\nsum(diag(A)) = sum(λi)\n', check, '≈', sum(Lambda))
print('\n|A| = sum(λi)\n', np.linalg.det(a), '≈', np.product(Lambda))
print('\ntr(A ** 2) = sum(λi ** 2)\n', np.dot(a, a).trace(), '≈', np.sum(np.array(Lambda) ** 2))
