import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def plotfunc(func, start=-10.0, finish=10.0, num=200, xticks=1, yticks=1):
    fig, ax = plt.subplots()
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.grid(True)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(xticks))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(yticks))

    xs = np.linspace(start, finish, num)
    ax.plot(xs, [func(x) for x in xs])
    plt.show()


def interface(func, extra_arg=None):
    print("Введите значение a и b:", end=' ')
    a, b = map(float, input().split())
    if extra_arg:
        print(
            f"Введите значение {func.__code__.co_varnames[extra_arg - 1]}:",
            end=' ')
        try:
            arg = int(input())
        except BaseException:
            arg = None

        return a, b, arg

    return a, b


def derivative(func, x, h=1e-5):
    return (func(x + h) - func(x)) / h
