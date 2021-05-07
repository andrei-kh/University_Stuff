import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from inspect import getfullargspec
from sympy import plot_implicit, Eq, lambdify, diff
# from sympy.utilities.lambdify import lambdastr


# Функция для отрисовки графика
def plotfunc(func, start=-10, finish=10, num=200, xlim=None, ylim=True,
             xticks=1, yticks=1, e=1e-3,
             figAx=None, show=True, name=None):

    if figAx is None:
        fig, ax = plt.subplots()
    else:
        fig, ax = figAx

    ax.grid(which='major', axis='both', linestyle='-')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    if xticks:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(xticks))
    if yticks:
        ax.yaxis.set_major_locator(ticker.MultipleLocator(yticks))

    if xlim is None:
        xlim = (start, finish)
        ax.set_xlim(xlim)
    else:
        ax.set_xlim(xlim)

    if ylim is True:
        ax.set_ylim(xlim)
    elif ylim is not None:
        ax.set_ylim(ylim)

    xs = np.linspace(start, finish, num)

    if name is not None:
        ax.plot(xs, [func(x) for x in xs], label=name)
    else:
        ax.plot(xs, [func(x) for x in xs])

    if show:
        if name is not None:
            plt.legend(loc='upper left')
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


def print_table(table, headers, e='.3f'):
    new_table = [headers]
    max_h_len = [len(_) for _ in headers]
    for i in range(len(table)):
        new_table.append([])
        for j in range(len(table[0])):
            if isinstance(table[i][j], str):
                new_table[-1].append(table[i][j])
            elif isinstance(table[i][j], int):
                new_table[-1].append(str(table[i][j]))
            else:
                new_table[-1].append(str(format(table[i][j], e)))

            max_h_len[j] = max(max_h_len[j], len(new_table[-1][j]))

    headers_str = "| "
    for i in range(len(new_table[0])):
        half1 = (max_h_len[i] - len(new_table[0][i])) // 2
        half2 = max_h_len[i] - half1 - len(new_table[0][i])
        headers_str += ' ' * half2 + new_table[0][i] + ' ' * half1 + ' | '
    print(headers_str)
    print('-' * (len(headers_str) - 1))

    for r in new_table[1:]:
        print('| ', end='')
        for i in range(len(r)):
            half1 = (max_h_len[i] - len(r[i])) // 2
            half2 = max_h_len[i] - half1 - len(r[i])
            print(' ' * half2 + r[i] + ' ' * half1, end=' | ')
        print()


def print_finite_diffs(finite_diffs):
    for i in range(len(finite_diffs[0])):
        for j in range(len(finite_diffs)):
            try:
                print(format(finite_diffs[j][i], '.4f'), end=' ')
            except BaseException:
                continue
        print()
