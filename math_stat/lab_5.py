def task(values, F_crit):
    n, m = len(values), len(values[0])
    xj_sums = [sum(col) / n for col in zip(*values)]
    x_sum = sum(xj_sums) / m

    Q_a = n * sum((xj_sum - x_sum) ** 2 for xj_sum in xj_sums)
    Q_o = sum((val - xj_sum) ** 2 for col, xj_sum in zip(zip(*values), xj_sums) for val in col)
    Q = Q_a + Q_o
    D = Q_a / Q

    SA2 = Q_a / (m - 1)
    SO2 = Q_o / (m * (n - 1))
    F = SA2 / SO2

    print(f"x = {x_sum}")
    print(f"Qa = {Q_a}")
    print(f"Qo = {Q_o}")
    print(f"Q = {Q}")
    print(f"{F} > {F_crit} -> влияет")
    print(f"D = {D}")


def task_1():
    values = [
        [140, 150, 148, 150],
        [144, 149, 149, 155],
        [142, 152, 146, 154],
        [145, 152, 147, 152]
    ]

    print("Задаине 1.")
    task(values, 3.49)


def task_2():
    values = [
        [28, 39, 41],
        [33, 52, 49],
        [42, 53, 56],
        [47, 54, 62],
        [48, 56, 63],
        [50, 58, 64],
        [50, 59, 65],
        [51, 63, 72],
        [60, 64, 77],
        [71, 77, 87]
    ]

    print("Задаине 2.")
    task(values, 3.35)


def task_3():
    values = [
        [0.9, 1, 1.3, 1.8],
        [0.8, 0.7, 1.5, 1.9],
        [1, 1.3, 1.6, 1.1],
        [1.3, 1, 1.4, 1.4],
        [1.4, 1.3, 1.2, 1.3],
        [0.8, 1.3, 1.1, 1.9]
    ]

    print("Задаине 3.")
    task(values, 3.10)


if __name__ == '__main__':
    task_1()
    print()
    task_2()
    print()
    task_3()
