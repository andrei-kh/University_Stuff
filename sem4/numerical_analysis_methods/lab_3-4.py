# Variant 24
from util import EqSystem
from sympy.abc import x, y
from sympy import cos, sin, lambdify, solve, Symbol, Matrix


systemA = EqSystem([cos(x) + y - 1.2, 2 * x - sin(y - 0.5) - 2])
systemB = EqSystem([sin(x + y) - 1.2 * x + 0.2, x**2 + y**2 - 1])


# Метод Ньютона
def newtonMethod(system, x0, y0, e=1e-3):
    i = 0
    while not system.test_accuracy([x0, y0]):
        i += 1
        pdiffs = system.get_pdiffs([x0, x0])
        f1, f2 = [leq(x0, y0) for leq in system.leqs]
        J = float(Matrix(pdiffs).det())

        A1 = float(Matrix([[f1, pdiffs[0][1]], [f2, pdiffs[1][1]]]).det())
        x0 = x0 - A1 / J

        A2 = float(Matrix([[pdiffs[0][0], f1], [pdiffs[1][0], f2]]).det())
        y0 = y0 - A2 / J

    return (x0, y0), i


# Метод Итераций
def iterationMethod(system, x0, y0, e=1e-3):
    diffs = system.get_pdiffs([x0, y0])

    l11, l12, l21, l22 = Symbol('l11'), Symbol('l12'), Symbol('l21'), Symbol('l22')

    l1 = solve([1 + diffs[0][0] * l11 + diffs[1][0] * l12, l11 * diffs[0][1] + l12 * diffs[1][1]])
    l2 = solve([diffs[0][0] * l21 + diffs[1][0] * l22, 1 + l21 * diffs[0][1] + l22 * diffs[1][1]])

    x_func = lambdify((x, y), x + l1[l11] * system.eqs[0] + l1[l12] * system.eqs[1])
    y_func = lambdify((x, y), y + l2[l21] * system.eqs[0] + l2[l22] * system.eqs[1])

    i = 0
    while not system.test_accuracy([x0, y0]):
        i += 1
        x0 = x_func(x0, y0)
        y0 = y_func(x0, y0)

    return (x0, y0), i


if __name__ == '__main__':
    systemA.plot_system()
    systemA.format({"Метод Ньютона:": newtonMethod})
    systemA.plot_system()
    systemB.plot_system()
    systemB.format({"Метод Итерации:": iterationMethod}, 2)
    systemB.plot_system()
