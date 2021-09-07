# Variant 24

from sympy import lambdify, Symbol, exp, log
from sympy.solvers import solve
from util import plotfunc
import matplotlib.pyplot as plt


def linear_function(p):
    n = len(p)
    a0, a1 = Symbol('a0'), Symbol('a1')
    x_sum = sum([pi[0] for pi in p])
    y_sum = sum([pi[1] for pi in p])
    xy_sum = sum([pi[0] * pi[1] for pi in p])
    x_sum_squared = sum([pi[0]**2 for pi in p])

    eq1 = n * a0 + a1 * x_sum - y_sum
    eq2 = a0 * x_sum + a1 * x_sum_squared - xy_sum
    solution = solve((eq1, eq2), a0, a1)

    x = Symbol('x')
    func = solution[a0] + solution[a1] * x
    return lambdify([x], func)


def qadratic_function(p):
    n = len(p)
    a, b, c = Symbol('a'), Symbol('b'), Symbol('c')
    Mx = 1 / n * sum([pi[0] for pi in p])
    Mx2 = 1 / n * sum([pi[0] ** 2 for pi in p])
    Mx3 = 1 / n * sum([pi[0] ** 3 for pi in p])
    Mx4 = 1 / n * sum([pi[0] ** 4 for pi in p])
    My = 1 / n * sum([pi[1] for pi in p])
    Mxy = 1 / n * sum([pi[0] * pi[1] for pi in p])
    Mx2y = 1 / n * sum([pi[0] * pi[0] * pi[1] for pi in p])

    eq1 = Mx4 * a + Mx3 * b + Mx2 * c - Mx2y
    eq2 = Mx3 * a + Mx2 * b + Mx * c - Mxy
    eq3 = Mx2 * a + Mx * b + n * c - My
    solution = solve((eq1, eq2, eq3), a, b, c)

    x = Symbol('x')
    func = solution[a] * x * x + solution[b] * x + solution[c]
    return lambdify([x], func)


def exponential_function(p):
    a0, a1 = Symbol('a0'), Symbol('a1')
    y_sum = sum([pi[1] for pi in p])
    xy_sum = sum([pi[0] * pi[1] for pi in p])
    xy_sum_squared = sum([(pi[0]**2) * pi[1] for pi in p])
    ylny_sum = sum([pi[1] * log(pi[1]) for pi in p])
    xylny_sum = sum([pi[0] * pi[1] * log(pi[1]) for pi in p])

    eq1 = y_sum * a0 + a1 * xy_sum - ylny_sum
    eq2 = a0 * xy_sum + a1 * xy_sum_squared - xylny_sum

    solution = solve((eq1, eq2), a0, a1)

    x = Symbol('x')
    func = exp(solution[a0]) * exp(x * solution[a1])

    return lambdify([x], func)


def logariphmic_function(p):
    n = len(p)
    a0, a1 = Symbol('a0'), Symbol('a1')
    x_sum = sum([log(pi[0]) for pi in p])
    y_sum = sum([pi[1] for pi in p])
    xy_sum = sum([log(pi[0]) * pi[1] for pi in p])
    x_sum_squared = sum([log(pi[0]) ** 2 for pi in p])

    eq1 = n * a0 + a1 * x_sum - y_sum
    eq2 = a0 * x_sum + a1 * x_sum_squared - xy_sum

    solution = solve((eq1, eq2), a0, a1)

    x = Symbol('x')
    func = solution[a0] + solution[a1] * log(x)
    return lambdify([x], func)


def hiperbolic_function(p):
    n = len(p)
    a0, a1 = Symbol('a0'), Symbol('a1')
    x_sum = sum([1 / pi[0] for pi in p])
    y_sum = sum([pi[1] for pi in p])
    xy_sum = sum([1 / pi[0] * pi[1] for pi in p])
    x_sum_squared = sum([1 / (pi[0]**2) for pi in p])

    eq1 = n * a0 + a1 * x_sum - y_sum
    eq2 = a0 * x_sum + a1 * x_sum_squared - xy_sum

    solution = solve((eq1, eq2), a0, a1)

    x = Symbol('x')
    func = solution[a0] + solution[a1] / x
    return lambdify([x], func)


def draw_func(func, points, fig, ax, name, show=False):
    ax.set_title("Графики")
    plt.scatter([p[0] for p in points], [p[1] for p in points], color='r')
    plotfunc(
        func, -30, 30, 200000, (-30, 30),
        (-100, 100),
        figAx=(fig, ax),
        show=show, xticks=None, yticks=None, name=name)


if __name__ == "__main__":
    points = [
        (0.22, 58.46),
        (-3.05, 36.05),
        (-1.76, 31.17),
        (-1.25, 16.17),
        (-0.45, 11.16),
        (-0.8, 69.23),
        (-0.26, 58.08),
        (-3.07, 43.13)
    ]

    log_points = [
        (1, 6),
        (2, 7.45),
        (5, 8.24),
        (8, 12.46),
        (9, 13.09),
        (12, 14.56),
        (14, 25.89),
        (16, 29.91)
    ]

    fig, ax = plt.subplots()
    lin_func = linear_function(points)
    qud_func = qadratic_function(points)
    exp_func = exponential_function(points)
    log_func = logariphmic_function(points)
    hip_func = hiperbolic_function(points)

    draw_func(lin_func, points, fig, ax, "Линейная функция")
    draw_func(qud_func, points, fig, ax, "Многочлен второй степени")
    draw_func(exp_func, points, fig, ax, "Показательная функция")
    draw_func(log_func, points, fig, ax, "Логарифмическая функция")
    draw_func(hip_func, points, fig, ax, "Гиперболическая функция", show=True)

    lin_func = linear_function(log_points)
    qud_func = qadratic_function(log_points)
    exp_func = exponential_function(log_points)
    log_func = logariphmic_function(log_points)
    hip_func = hiperbolic_function(log_points)

    fig, ax = plt.subplots()
    draw_func(lin_func, log_points, fig, ax, "Линейная функция")
    draw_func(qud_func, log_points, fig, ax, "Многочлен второй степени")
    draw_func(exp_func, log_points, fig, ax, "Показательная функция")
    draw_func(log_func, log_points, fig, ax, "Логарифмическая функция")
    draw_func(hip_func, log_points, fig, ax, "Гиперболическая функция", show=True)