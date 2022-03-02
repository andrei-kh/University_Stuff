import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# from sympy.utilities.lambdify import lambdastr


# Функция для отрисовки графика
def plotfunc(func, start=-10, finish=10, num=200, xlim=None, ylim=True,
             xticks=1, yticks=1, figAx=None, show=True, name=None):

    if figAx is None:
        _, ax = plt.subplots()
    else:
        _, ax = figAx

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
