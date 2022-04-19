from sympy import Symbol, solve
from math import log
from typing import List, Tuple
import matplotlib.pyplot as plt

def log_interpolation(x: List[int], y: List[int]) -> Tuple[int, int]:
    """
    Функция используемая для логарифмической интерполяции.

    Arguments:
        x {List[int]} -- x координаты
        y {List[int]} -- y координаты

    Returns:
        Tuple[int, int] -- коэффициенты a, b в формуле a + b * log(x)
    """
    n = len(x)
    a0, a1 = Symbol('a0'), Symbol('a1')
    x_sum = sum([log(xi) for xi in x])
    y_sum = sum([yi for yi in y])
    xy_sum = sum([log(xi) * yi for xi, yi in zip(x, y)])
    x_sum_squared = sum([log(xi) ** 2 for xi in x])

    eq1 = n * a0 + a1 * x_sum - y_sum
    eq2 = a0 * x_sum + a1 * x_sum_squared - xy_sum

    solution = solve((eq1, eq2), a0, a1)

    return solution[a0], solution[a1]


def extended_gcd(a: int, b: int) -> int:
    """
    Расширенный алгоритм евклида, в котором считается кол-во операций умножения и деления.

    Arguments:
        a {int} -- первое число
        b {int} -- второе число

    Returns:
        int -- кол-во операций умножения и деления
    """
    div_mul_operations = 0
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    div_mul_operations += 1
    q = a0 // b0
    div_mul_operations += 1
    r = a0 - q * b0
    while r > 0:
        div_mul_operations += 1
        temp = t0 - q * t
        t0 = t
        t = temp
        div_mul_operations += 1
        temp = s0 - q * s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        div_mul_operations += 1
        q = a0 // b0
        div_mul_operations += 1
        r = a0 - q * b0
    return div_mul_operations


if __name__ == "__main__":
    NUMBER_OF_POINTS = 101
    fib_numbers = [1, 1]
    # находим числа фибоначчи
    for i in range(2, NUMBER_OF_POINTS):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
    number_of_operations = []
    div_operations = []
    # Находим кол-во операций умножения и деления для каждой пары последующих чисел фибоначчи
    for i in range(1, NUMBER_OF_POINTS):
        number_of_operations.append(extended_gcd(fib_numbers[i - 1], fib_numbers[i]))
    # выбираем все числа фибоначчи кроме последнего
    fib_numbers = fib_numbers[:NUMBER_OF_POINTS - 1]
    # находим коэффициенты логарифмической интерполяции
    a, b = log_interpolation(fib_numbers, number_of_operations)
    print(f"Формула для количество операций деления и умножения: {a} + {b} * log(x)")
    # рисуем графики функций
    plt.xlabel("Значение числа фибоначчи")
    plt.ylabel("Количество операций")
    plt.plot(fib_numbers, number_of_operations, label='Количество операций деленияи и умножения')
    plt.plot(fib_numbers, [a + b * log(x) for x in fib_numbers], label='Логарифмическая интерполяция операций деления и умножения')
    plt.legend()
    plt.show()
