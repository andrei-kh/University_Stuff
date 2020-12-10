import numpy as np
from sympy import Symbol
from sympy.solvers import solveset
from sympy import pprint
from sympy import init_printing

init_printing()
A = [[5, 6, 6],
     [2, 3, 3],
     [1, 4, 8]]


a = np.array(A, dtype=float)
print('Матрица А:\n', a)

M = np.zeros(a.shape)
c = [0] * (a.shape[1] + 1)
c[a.shape[0]] = 1

for k in range(1, a.shape[0] + 1):
    M = np.dot(a, M) + c[a.shape[0] - k + 1] * np.identity(a.shape[0])
    c[a.shape[0] - k] = - 1 / k * np.trace(np.dot(a, M))

x = Symbol('x')
print('\nХарактеристическое уравнение:')
Lambda = c[3] * x ** 3 + c[2] * x ** 2 + c[1] * x + c[0]
pprint(Lambda)

Lambda = list(solveset(Lambda))
print('\nСобственные значения:')
print(*Lambda)

check = a.trace()
print('\nПроверка:')
print('\nsum(diag(A)) = sum(λi)\n', check, '≈', sum(Lambda))
print('\n|A| = sum(λi)\n', np.linalg.det(a), '≈', np.product(Lambda))
print('\ntr(A ** 2) = sum(λi ** 2)\n', np.dot(a, a).trace(), '≈', np.sum(np.array(Lambda) ** 2))