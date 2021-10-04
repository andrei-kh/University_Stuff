from math import log, cos
import matplotlib.pyplot as plt
from utils import print_table


def task(a=1.5, b=4.5, f0=1.1, h=0.1):
    # вариант 24
    def func(x, y):
        return y / log(y) + cos(x)

    ad2, t = adams_2(func, h, a, b, f0)
    ad3, t = adams_3(func, h, a, b, f0)
    ad4, t = adams_4(func, h, a, b, f0)

    # таблица результатов
    table = []
    for i in range(len(ad2)):
        table.append([t[i], ad2[i], ad3[i], ad4[i]])

    print(' Метод Адамса')
    print_table(table, ['t', 'm = 2', 'm = 3', 'm = 4'], '.6f')

    # графики
    fig, ax = plt.subplots()
    ax.set_title("Метод Адамса")

    plt.plot(t, ad2, marker='o', color='r', label='m = 2')
    plt.plot(t, ad3, marker='o', color='g', label='m = 3')
    plt.plot(t, ad4, marker='o', color='b', label='m = 4')

    plt.xlabel('t')
    plt.ylabel('y')

    plt.legend()
    plt.show()


def adams_2(f, h, a, b, f0):
    n = int((b - a) / h)
    t = [a + i * h for i in range(0, n + 1)]
    y = [f0]

    # метод Рунге-Кутта
    k1 = f(t[0], y[0])
    k2 = f(t[0] + h, y[0] + h * k1)
    y1 = y[0] + h / 2 * (k1 + k2)
    y.append(y1)

    for i in range(1, n):
        y_next = y[i] + h / 2 * (3 * f(t[i], y[i]) - f(t[i - 1], y[i - 1]))
        y.append(y_next)

    return y, t


def adams_3(f, h, a, b, f0):
    n = int((b - a) / h)
    t = [a + i * h for i in range(0, n + 1)]
    y = [f0]

    # метод Рунге-Кутта
    for i in range(2):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(t[i] + h, y[i] - h * k1 + 2 * k2 * h)
        y_next = y[i] + h / 6 * (k1 + 4 * k2 + k3)
        y.append(y_next)

    b1, b2, b3 = 23 / 12, -4 / 3, 5 / 12
    for i in range(2, n):
        fn_1 = f(t[i], y[i])
        fn_2 = f(t[i - 1], y[i - 1])
        fn_3 = f(t[i - 2], y[i - 2])
        y_next = y[i] + h * (b1 * fn_1 + b2 * fn_2 + b3 * fn_3)
        y.append(y_next)

    return y, t


def adams_4(f, h, a, b, f0):
    n = int((b - a) / h)
    t = [a + i * h for i in range(0, n + 1)]
    y = [f0]

    # метод Рунге-Кутта
    for i in range(3):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(t[i] + h / 2, y[i] + h / 2 * k2)
        k4 = f(t[i] + h, y[i] + h * k3)

        y_next = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

        y.append(y_next)

    b1, b2, b3, b4 = 55 / 24, -59 / 24, 37 / 24, -3 / 8
    for i in range(3, n):
        fn_1 = f(t[i], y[i])
        fn_2 = f(t[i - 1], y[i - 1])
        fn_3 = f(t[i - 2], y[i - 2])
        fn_4 = f(t[i - 3], y[i - 3])
        y_next = y[i] + h * (b1 * fn_1 + b2 * fn_2 + b3 * fn_3 + b4 * fn_4)
        y.append(y_next)

    return y, t


task()
