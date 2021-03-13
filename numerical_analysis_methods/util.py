import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from inspect import getfullargspec
from sympy import plot_implicit, Eq, lambdify, diff
# from sympy.utilities.lambdify import lambdastr


# Функция для отрисовки графика
def plotfunc(func, start=-10.0, finish=10.0, num=200,
             xticks=1, yticks=1, set_ylim=True, e=1e-3):
    fig, ax = plt.subplots()
    ax.grid(which='major', axis='both', linestyle='-')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
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
    def __init__(self, func, methods_and_names, startin_args=['a', 'b']) -> None:
        self.methods_and_names = methods_and_names
        self.func = func
        self.default_args = ['f', 'a', 'b', 'e']
        self.starting_args = startin_args

    # Функция для интерфейса
    def get_params(self, method) -> list:
        print(
            f"Введите значение {self.starting_args[0]} и {self.starting_args[1]}:",
            end=' ')
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
                        args.append(float(input()))
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


# Класс систем уравнений
class EqSystem():
    def __init__(self, equations):
        self.eqs = equations
        self.params = sorted(list(equations[0].free_symbols), key=lambda s: s.name)
        self.leqs = [lambdify(self.params, eq) for eq in equations]
        self.default_args = ['system', 'e', *[str(p) + '0' for p in self.params]]
        self.pdiffs = {k: [lambdify(self.params, diff(v, k)) for v in self.eqs] for k in self.params}

    def get_pdiffs(self, vals):
        diffs = []

        for i in range(len(self.eqs)):
            diffs.append([self.pdiffs[p][i](*vals) for p in self.params])

        return diffs

    def test_accuracy(self, vals, e=1e-3, aim=0):
        for leq in self.leqs:
            if abs(leq(*vals)) > e:
                return False

        return True

    def __cmap_ints(self, i):
        return "#" + hex(((int(i) + 1) * 2396745) % (256**3))[2:].rjust(6, "0")

    def plot_system(self, *ranges):
        while len(ranges) < len(self.params):
            ranges += ((-5, 5),)

        curves = plot_implicit(Eq(self.eqs[0], 0),
                               *[(self.params[_],) + ranges[_] for _ in range(len(ranges))],
                               line_color=self.__cmap_ints(0), show=False)

        for i in range(1, len(self.eqs)):
            curves.append(
                plot_implicit(
                    Eq(self.eqs[i], 0),
                    *[(self.params[_],) + ranges[_] for _ in range(len(ranges))],
                    line_color=self.__cmap_ints(i), show=False)[0])

        curves.show()

    def format(self, method_and_names, roots=1, prec='.10f'):
        def __get_params(method):
            print(f"Введите значение {self.params[0]}0 и {self.params[1]}0:", end=' ')
            args = [self]
            args += list(map(float, input().split()))
            if len(args) > len(self.default_args):
                raise ValueError("Too many inputs")
            f_args = list(getfullargspec(method).args)
            if len(f_args) > len(self.default_args):
                for arg in f_args:
                    if arg not in self.default_args:
                        print(f"Введите значение {arg}:", end=' ')
                        try:
                            args.append(float(input()))
                        except BaseException:
                            args.append(None)

            return args

        for name, method in method_and_names.items():
            print(f'\n{name}')
            for r in range(roots):
                print(f"Для {r + 1}-го корня:")
                args = __get_params(method)
                value, iterarions = method(*args)
                for i in range(len(self.eqs)):
                    print(f"\tf{i + 1}{value} = {format(self.leqs[i](*value), prec)}")
                print("\tКоличество итераций:", iterarions)


# Вычисление первой производной
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


# Вычисление второй производной
def second_derivative(f, x, h=1e-5):
    return (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h * h)
