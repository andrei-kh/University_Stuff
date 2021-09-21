from utils import print_table
import matplotlib.pyplot as plt
from math import exp


def runge_kutt_2(f, h, a, b, f0):
    n = int((b - a) / h)
    t = [a + i * h for i in range(0, n + 1)]
    y = [f0]

    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h, y[i] + h * k1)

        y_next = y[i] + h / 2 * (k1 + k2)

        y.append(y_next)

    return y, t


def runge_kutt_3(f, h, a, b, f0):
    n = int((b - a) / h)
    t = [a + i * h for i in range(0, n + 1)]
    y = [f0]

    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(t[i] + h, y[i] - h * k1 + 2 * k2 * h)

        y_next = y[i] + h / 6 * (k1 + 4 * k2 + k3)

        y.append(y_next)

    return y, t


def runge_kutt_4(f, h, a, b, f0):
    n = int((b - a) / h)
    t = [a + i * h for i in range(0, n + 1)]
    y = [f0]

    for i in range(n):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h / 2, y[i] + h / 2 * k1)
        k3 = f(t[i] + h / 2, y[i] + h / 2 * k2)
        k4 = f(t[i] + h, y[i] + h * k3)

        y_next = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

        y.append(y_next)

    return y, t


def task_1(h=0.1, a=0.5, b=4.5, f0=2.2):
    def func(x, y):
        return x * x + 2 * x + y / x

    rk2, t = runge_kutt_2(func, h, a, b, f0)
    rk3, t = runge_kutt_3(func, h, a, b, f0)
    rk4, t = runge_kutt_4(func, h, a, b, f0)

    # таблица результатов
    table = []
    for i in range(len(rk2)):
        table.append([t[i], rk2[i], rk3[i], rk4[i]])

    print(' Метод Рунге-Кутта')
    print_table(table, ['t', 'm = 2', 'm = 3', 'm = 4'], '.6f')

    # графики
    fig, ax = plt.subplots()
    ax.set_title("Метод Рунге-Кутта")

    plt.plot(t, rk2, marker='o', color='r', label='m = 2')
    plt.plot(t, rk3, marker='o', color='g', label='m = 3')
    plt.plot(t, rk4, marker='o', color='b', label='m = 4')

    plt.xlabel('t')
    plt.ylabel('y')

    plt.legend()
    plt.show()


def euler_method(f, h, a, b, y0, z0):
    n = int((b - a) / h)

    t = [a + i * h for i in range(0, n + 1)]
    y = [y0]
    z = [z0]

    for i in range(n):
        f1, f2 = f(t[i], y[i], z[i])
        y_next = y[i] + h * f1
        z_next = y[i] + h * f2

        y.append(y_next)
        z.append(z_next)

    return y, z, t


def runge_kutt(f, h, a, b, y0, z0):
    n = int((b - a) / h)

    t = [a + i * h for i in range(0, n + 1)]
    y = [y0]
    z = [z0]

    for i in range(n):
        k1, l1 = f(t[i], y[i], z[i])
        k2, l2 = f(t[i] + h / 2, y[i] + h / 2 * k1, z[i] + h / 2 * l1)
        k3, l3 = f(t[i] + h / 2, y[i] + h / 2 * k2, z[i] + h / 2 * l2)
        k4, l4 = f(t[i] + h, y[i] + h * k3, z[i] + h * l3)

        y_next = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        z_next = z[i] + h / 6 * (l1 + 2 * l2 + 2 * l3 + l4)

        y.append(y_next)
        z.append(z_next)

    return y, z, t


def task_2(h=0.1, a=0, b=5, x0=-3, y0=-1):
    def func(t, x, y):
        x_dot = 2 * x + y - 3 * exp(4 * t)
        y_dot = x + 2 * y + 2 * exp(t)
        return x_dot, y_dot

    x_eul, y_eul, t = euler_method(func, h, a, b, x0, y0)
    x_run, y_run, t = runge_kutt(func, h, a, b, x0, y0)

    # таблица результатов
    table = []
    for i in range(len(t)):
        table.append([t[i], x_eul[i], y_eul[i], x_run[i], y_run[i]])

    print_table(table, ['t', 'x euler', 'y euler', 'x runge', 'y runge'])

    # графики
    fig, ax = plt.subplots()
    ax.set_title("Явный метод Эйлера и Метод Рунге-Кутта")

    plt.plot(t, x_eul, marker='o', color='red', label='x(t) euler')
    plt.plot(t, y_eul, marker='o', color='gray', label='y(t) euler')
    plt.plot(t, x_run, marker='o', color='pink', label='x(t) runge')
    plt.plot(t, y_run, marker='o', color='black', label='y(t) runge')

    plt.xlabel('t')
    plt.legend()
    plt.show()

task_1()
task_2()
