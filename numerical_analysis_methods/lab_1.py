# Variant 24
from util import plotfunc, derivative, interface
import numpy as np

np.seterr(divide='raise', invalid='raise')


def func(x):
    try:
        return 3 * np.log10(x) - 4 / (2 * x + 3)
    except BaseException:
        raise ValueError('Дано неверное значение функции')


def bisection_method(f, a, b, e=1e-5):

    if f(a) * f(b) >= 0 or a > b:
        raise ValueError('Дан Неверный отрезок')

    i = 0
    while a < b:
        x1 = (a + b) / 2
        fx1 = f(x1)
        if abs(fx1) < e:
            break
        if fx1 * f(a) < 0:
            b = x1
        elif fx1 * f(b) < 0:
            a = x1
        i += 1

    return x1, i


def iterative_method(f, a, b, M=None, e=1e-5):
    if f(a) * f(b) >= 0 or a > b:
        raise ValueError('Дан Неверный отрезок')

    if M is None:
        xs = np.arange(a, b, (b - a) / e)
        dxs = [abs(derivative(f, x)) for x in xs]
        lam = 1 / max(dxs)
    else:
        lam = 1 / M

    x = a
    i = 0
    while abs(func(x)) > e:
        x = x - lam * func(x)
        i += 1

    return x, i


def newtons_method(f, a, b, e=1e-5):
    if f(a) * f(b) >= 0 or a > b:
        raise ValueError('Дан неверный отрезок')

    x = a
    i = 0
    while abs(f(x)) > e:
        x = x - f(x) / derivative(f, x)
        i += 1

    return x, i


if __name__ == "__main__":
    try:
        plotfunc(func, 0.01, 20.0, 100)

        print("\nМетод бисекции:")
        args = interface(bisection_method)
        bisection, bisection_iterations = bisection_method(func, *args)
        print(f"f({bisection}) = {format(func(bisection), '.16f')}")
        print("Количество итераций:", bisection_iterations)

        print("\nМетод простых итераций:")
        args = interface(iterative_method, 4)
        iterarion, iteration_iterations = iterative_method(func, *args)
        print(f"f({iterarion}) = {format(func(iterarion), '.16f')}")
        print("Количество итераций:", iteration_iterations)

        print("\nМетод Ньютона:")
        args = interface(newtons_method)
        newton, newton_iterations = newtons_method(func, *args)
        print(f"f({newton}) = {format(func(newton), '.16f')}")
        print("Количество итераций:", newton_iterations)

        plotfunc(func, 0.01, 20.0, 100)
    except BaseException as e:
        print(e)
