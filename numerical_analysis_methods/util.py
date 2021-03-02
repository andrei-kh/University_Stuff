import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from inspect import getfullargspec


# Функция для отрисовки графика
def plotfunc(func, start=-10.0, finish=10.0, num=200,
             xticks=1, yticks=1, set_ylim=True):
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

    ax.set_xlim([start, finish])
    if set_ylim:
        ax.set_ylim([start, finish])

    xs = np.linspace(start, finish, num)
    ax.plot(xs, [func(x) for x in xs])
    plt.show()


# Класс интерфейса
class Formatter():
    def __init__(self, func, methods_and_names) -> None:
        self.methods_and_names = methods_and_names
        self.func = func
        self.default_args = ['f', 'a', 'b', 'e']

    # Функция для интерфейса
    def get_params(self, method) -> list:
        print("Введите значение a и b:", end=' ')
        args = [self.func]
        args += list(map(float, input().split()))
        if len(args) > len(self.default_args):
            raise ValueError("Too many inputs")

        f_args = list(getfullargspec(method).args)
        if len(f_args) > len(self.default_args):
            for arg in f_args:
                if arg not in self.default_args:
                    print(f"Введите значение {arg}:", end=' ')
                    try:
                        args.append(int(input()))
                    except BaseException:
                        args.append(None)

        return args

    # Функция интерфейса
    def interface(self, method, prec='.10f') -> None:
        args = self.get_params(method)
        value, iterarions = method(*args)
        print(f"f({value}) = {format(self.func(value), prec)}")
        print("Количество итераций:", iterarions)

    def interface_wrapper(self) -> None:
        print()
        for name, method in self.methods_and_names.items():
            print(f"\n{name}")
            self.interface(method)


# Вычисление первой производной
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


# Вычисление второй производной
def second_derivative(f, x, h=1e-5):
    return (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h * h)
