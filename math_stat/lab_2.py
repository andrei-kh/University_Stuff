import matplotlib.pyplot as plt


def draw_histogram(data, intervals, r_freqs, name):
    plt.title(name)
    plt.xticks(data)
    plt.yticks(r_freqs)
    plt.hist(data, bins=intervals, weights=r_freqs)
    plt.show()


def draw_graph(x, y, name):
    plt.title(name)
    plt.xticks(x)
    plt.yticks(y)
    plt.plot(x, y, marker='o')
    plt.show()


def task1():
    # интервалы
    intervals = [0, 24, 25, 49, 50, 74, 75, 99, 100, 124, 125, 149, 150, 174, 175, 199, 200, 299, 300, 399]

    # абсолютные частоты (ni)
    freqs = [0, 1, 3, 6, 7, 6, 5, 4, 8, 4]

    # объем выборки (n)
    volume = sum(freqs)

    # середины отрезков
    middles = [(intervals[i] + intervals[i + 1]) / 2 for i in range(0, len(intervals) - 1, 2)]

    # выборочное среднее
    chosen_middle = sum([f * m for f, m in zip(freqs, middles)]) / volume
    print("Выборочное среднее:", chosen_middle)

    # выборочная дисперсия
    dispersion = sum([(chosen_middle - m) ** 2 * f for f, m in zip(freqs, middles)]) / (volume - 1)
    print("Выборочная дисперсия:", dispersion)

    # отрисовка гистограммы частот
    draw_histogram(middles, intervals, freqs, name='Гистограмма частот')

    # накопленные частоты (сумма до i-го)
    m = [sum(freqs[:i + 1]) for i in range(len(freqs))]

    # эмпирическая функция
    Fn = [mx / volume for mx in m]

    # отрисовка графика эмпирической функции распределения
    draw_graph(intervals[1::2], Fn, name='Эмпирическая функция распределения')

    # отрисовка полигона частот
    draw_graph(middles, freqs, name='Полигон частот')


def task2():
    # интервалы
    intervals = [15, 17, 19, 21, 23, 25, 27]

    # абсолютные частоты (ni)
    freqs = [100, 300, 500, 700, 600, 300]

    # объем выборки (n)
    volume = sum(freqs)

    # относительные частоты (ni / n)
    relative_freqs = [f / volume for f in freqs]

    # отрисовка гистограммы относительных частот (ноль для отрисовки)
    draw_histogram(intervals, intervals, relative_freqs + [0], name='Гистограмма относительных частот')

    # накопленные частоты (сумма до i-го)
    m = [sum(freqs[:i + 1]) for i in range(len(freqs))]

    # эмпирическая функция
    Fn = [mx / volume for mx in m]

    # отрисовка графика эмпирической функции распределения
    draw_graph(intervals[:-1], Fn, name='Эмпирическая функция распределения')

    # середины отрезков
    middles = [(intervals[i] + intervals[i + 1]) / 2 for i in range(len(intervals) - 1)]

    # отрисовка полигона относительных частот
    draw_graph(middles, relative_freqs, name='Полигон относительных частот')


if __name__ == "__main__":
    print("Задание 1")
    task1()
    print("Задание 2")
    task2()
