# Variant 24
from util import Formatter, plotfunc, derivative
import numpy as np

np.seterr(divide='raise', invalid='raise')


# Функция варианта 24
def func(x):
    try:
        return 3 * np.log10(x) - 4 / (2 * x + 3)
    except BaseException:
        return None


# Метод бисекции
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


# Метод простой итерации
def iterative_method(f, a, b, M=None, e=1e-5):
    if f(a) * f(b) >= 0 or a > b:
        raise ValueError('Дан Неверный отрезок')

    # Если значение M не указано M считается как max(f'(x))
    if M is None:
        xs = np.linspace(a, b, int((b - a) / e))
        dxs = [abs(derivative(f, x)) for x in xs]
        lam = 1 / max(dxs)
    else:
        lam = 1 / M

    x = a
    i = 0
    while abs(f(x)) > e:
        x = x - lam * func(x)
        i += 1

    return x, i


# Метод ньютона
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
        plotfunc(func, 0.1, 10.0, 100000, set_ylim=False)

        formatter = Formatter(func,
                              {"\nМетод бисекции:": bisection_method,
                               "Метод простых итераций:": iterative_method,
                               "Метод Ньютона:": newtons_method})
        formatter.interface_wrapper()

        plotfunc(func, 0.1, -10.0, 100000, set_ylim=False)
    except BaseException as e:
        print(e)
