import matplotlib.pyplot as plt
from math import ceil, sqrt, floor


def plot(values, b0, b1):
    x, y = zip(*values)

    _, ax = plt.subplots()
    plt.title("Диаграмма рассеивания")
    ax.set_xlim(0)
    ax.set_ylim(0)
    plt.xticks(range(0, ceil(max(x)) + 2, 1))
    plt.yticks(range(0, ceil(max(y)) + 20, 10))

    x_eq = range(floor(min(x)), ceil(max(x)) + 1)
    y_eq = [b0 + b1 * xi for xi in x_eq]
    ax.plot(x_eq, y_eq, color='red')
    ax.scatter(x, y)
    plt.show()


def calculations(values):
    x, y = zip(*values)
    n = len(values)

    x_sum = sum(x)
    y_sum = sum(y)
    xy_sum = sum(x * y for x, y in values)
    x_square_sum = sum(xi * xi for xi in x)

    b1 = (xy_sum - x_sum * y_sum / n) / (x_square_sum - x_sum ** 2 / n)
    b0 = (y_sum - b1 * x_sum) / n
    y_overline = [b0 + b1 * xi for xi in x]
    Q_rem = sum((yi - yoi) ** 2 for yi, yoi in zip(y, y_overline))
    Q_gen = sum((yi - y_sum / n) ** 2 for yi in y)
    Q_reg = Q_gen - Q_rem
    R_sqr = 1 - Q_rem / Q_gen
    R = sqrt(R_sqr)
    F_spec = Q_reg / (Q_rem / (n - 2))

    return R, R_sqr, b0, b1, F_spec


def task(values, F_crit):
    R, R_sqr, b0, b1, F_spec = calculations(values)

    print("3. Выборочный коэффициент корреляции:")
    print(f"R = {R}")
    print("4. Коэффициент детерминациии:")
    print(f"R^2 = {R_sqr}")
    print("5. Уравнение регрессии:")
    print(f"y = {b1}x + {b0}")
    print("6. Критическое распределение Фишера")
    print(f"Fкр = {F_crit}")
    print("7. Проверка качества регрессионной модели")
    print(f"Fнабл = {F_spec}")
    print(f"{F_spec} < {F_crit} -> уравнение регрессии качественное.")
    # диаграмма рассеивания и уравнение регрессии
    plot(values, b0, b1)


def task_1():
    # изначальные значения
    values = [
        (4.5, 68.8),
        (5.9, 58.3),
        (5.7, 62.6),
        (7.2, 52.1),
        (6.2, 54.5),
        (6.0, 57.1),
        (7.8, 51.0),
        (7.5, 50.7),
        (8.1, 48.6),
        (7.9, 49.1)
    ]
    print("Задание 1.")
    task(values, 238.88)


def task_2():
    # изначальные значения
    values = [
        (13.37, 158.53),
        (17.06, 213.96),
        (21.66, 272.1),
        (27.5, 322.3),
        (37.86, 410.51),
        (25.9, 354.99),
        (29.7, 420.31),
        (46.7, 407.84),
        (50.6, 438.19),
        (44, 573.98),
        (43.1, 592.98),
        (33, 444.26),
        (29.6, 362.63)
    ]
    print("Задание 2.")
    task(values, 242.98)

if __name__ == "__main__":
    task_1()
    print()
    task_2()
