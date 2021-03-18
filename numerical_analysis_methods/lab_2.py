# Variant 24
from util import plotfunc, derivative, Formatter, second_derivative
import numpy as np
from math import exp, cos


def func(x):
    try:
        return exp(x) - 3 - cos(x)
    except BaseException:
        return None


# Метод Хорд
def secant_method(f, a, b, e=1e-5):
    if f(a) * f(b) >= 0 or a > b:
        raise ValueError('Дан Неверный отрезок')

    if f(a) * second_derivative(f, a) < 0:
        def step():
            return x0 - (f(x0) / (f(b) - f(x0))) * (b - x0)
        x0 = a
    else:
        def step():
            return a - (f(a) / (f(x0) - f(a))) * (x0 - a)
        x0 = b

    i = 0
    while abs(f(x0)) > e:
        i += 1

        x1 = step()
        x0 = x1

    return x0, i


# Метод Эйткена
def aitken_method(f, a, b, M=None, e=1e-5):
    # Если значение M не указано M считается как max(f'(x))
    if M is None:
        xs = np.linspace(a, b, int((b - a) / e))
        dxs = [abs(derivative(f, x)) for x in xs]
        lam = 1 / max(dxs)
        print(f"Found M = {max(dxs)}")
        plotfunc(lambda x: derivative(func, x), -10, 10, 1000)
    else:
        lam = 1 / M

    def phi(x):
        return x - lam * f(x)

    i = 0
    x0 = a
    x1 = phi(x0)
    while True:
        i += 1
        x2 = phi(x1)
        x2_ = (x0 * x2 - x1 * x1) / (x2 - 2 * x1 + x0)
        x3 = phi(x2_)
        if abs(f(x3)) <= e:
            break
        x0 = x2_
        x1 = x3

    return x3, i


# Метод Стеффенсона
def stefensen_method(f, a, b, e=1e-5):
    i = 0
    x0 = a
    while abs(f(x0)) > e:
        x1 = x0 - (f(x0) * f(x0)) / (f(x0) - f(x0 - f(x0)))
        x0 = x1
        i += 1

    return x1, i


if __name__ == "__main__":
    plotfunc(func, -10, 10, 10000)
    fromatter = Formatter(func,
                          {"Метод Хорд:": secant_method,
                           "Метод Эйткена:": aitken_method,
                           "Метод стеффенсена:": stefensen_method})
    fromatter.interface_wrapper()

    plotfunc(func, -10, 10, 1000)
