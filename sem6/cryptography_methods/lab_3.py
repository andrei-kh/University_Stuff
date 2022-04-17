from math import sqrt, ceil
from typing import Callable, List, Tuple
from functools import reduce


def binary_pow(a: int, d: int, mod: int) -> int:
    """
    Алгоритм бинарного возведения в степень.

    Arguments:
        a {int} -- основание
        d {int} -- степень
        mod {int} -- модуль

    Returns:
        int -- результат
    """
    # Если степень равна 0, то результат равен 1
    if d == 0:
        return 1
    # представление d в двоичной ситсеме
    # функция bin() возвращает строку вида '0b1010'
    # поэтому представление в двоичной системе начинается со 2 символа
    d = bin(d)[2:]
    r = len(d) - 1
    # создадим массив a_i
    a_ = [0] * (r + 1)
    # положим a_0 = a
    a_[0] = a
    # вычисляем a_i для i = 1,...,r, r = len(d) - 1
    for i in range(1, r + 1):
        # вычисляем a_i
        a_[i] = (a_[i - 1] ** 2) * (a ** int(d[i]))
        # берем остаток по модулю
        a_[i] %= mod
    # возвращаем a_r по модулю для случаев когда d = 1
    return a_[r] % mod


def ord(a: int, p: int) -> int:
    """
    Вычисляет порядок числа `a` по модулю `p`.

    Arguments:
        a {int} -- первое число
        p {int} -- модуль

    Returns:
        int -- порядок числа
    """
    for i in range(1, p):
        if binary_pow(a, i, p) == 1:
            return i


def matching_method(a: int, b: int, p: int) -> int:
    """
    Метод согласования для решения задачи дискретного логарифмирования.

    Arguments:
        a {int} -- первое число
        b {int} -- второе число
        p {int} -- модуль

    Returns:
        int -- число x, удовлетворяющее сравнению a^x = b (mod p)
    """
    # Находим порядок числа a по модулю p
    ord_pa = ord(a, p)
    # Находим h
    h = ceil(sqrt(ord_pa))
    # Таблица значений величины ba^t (mod p), t = 0, 1, ..., h - 1
    bat_table = [(b * binary_pow(a, t, p)) % p for t in range(h)]
    # Вычисляем значений величины (a ^ h) ^ l (mod p), t = 1, 2, ..., h и сравниваем с значениями в таблице
    for l in range(1, h + 1):
        ahl = binary_pow(a, h * l, p)
        for t in range(h):
            # Если значения равны, то возвращаем x = h * l - t
            if ahl == bat_table[t]:
                return h * l - t


def find_all_prime_numbers_in_range(start: int, finish: int) -> List[int]:
    """
    Находит все простые числа на заданном промежутке `[start, finish]`.
    Для нахождения простых чисел используется модифицированное Решето Эратосфена.

    Arguments:
        start {int} -- начало промежутка
        finish {int} -- конец промежутка

    Returns:
        List[int] -- список простых чисел
    """
    # Список простых чисел на интервале
    primes = []
    # Список в котором True - число простое, False - число составное
    is_prime = [True] * (finish + 1)
    # 0 и 1 не простые
    is_prime[0] = is_prime[1] = False
    # решето Эратосфена i - число, is_prime_i - простое или нет
    for i, is_prime_i in enumerate(is_prime):
        if is_prime_i:
            # добавляем простое число в список, если оно в интервале
            if i >= start:
                primes.append(i)
            # все числа от i * i до finish с шагом i кратны i
            for j in range(i * i, finish + 1, i):
                is_prime[j] = False
    return primes


def factorize(number: int) -> List[int]:
    """
    Расскладывает число на множетели вида p1^a1, p2 ^a2 ....

    Arguments:
        number {int} -- число для разложения

    Returns:
        List[int] -- список множителей
    """
    # Находим простые до number
    primes = find_all_prime_numbers_in_range(1, number)
    # Список множителей
    factors = []
    # Проходим по всем простым числам
    for prime in primes:
        # Если остаток от деления на простое число не равен нулю, то переходим к следующему простому числу
        if number % prime != 0:
            continue
        factor = 1
        # Делим число на простое число
        while number % prime == 0:
            number //= prime
            factor *= prime
        # Добавляем множитель в список
        factors.append(factor)
    return factors


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Расширенный алгоритм евклида.

    Arguments:
        a {int} -- первое число
        b {int} -- второе число

    Returns:
        Tuple[int, int, int] -- три числа НОД(a, b), x, y, такие что НОД(a, b) = ax + by
    """
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    q = a0 // b0
    r = a0 - q * b0
    while r > 0:
        temp = t0 - q * t
        t0 = t
        t = temp
        temp = s0 - q * s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = a0 // b0
        r = a0 - q * b0
    r = b0
    return r, s, t


def modular_inv(number: int, mod: int) -> int:
    """
    Находит обратное по модулю `mod` для `number`.

    Arguments:
        number {int} -- число
        mod {int} -- модуль

    Returns:
        int -- обратное по модулю число
    """
    # Находим НОД модуля и числа и коэффициенты соотношения Безу
    # используя расширенный алгоритм евклида.
    gcd, x, y = extended_gcd(number, mod)
    # если НОД не равен 1, то обратного числа нет
    if gcd != 1:
        raise ValueError('Обратного числа не существует')
    # для отрицательных чисел нужно прибавить модуль
    return (x % mod + mod) % mod


def chineese_remainder_theorem(a: List[int], m: List[int]) -> int:
    """
    Китайская теорема об остатках.

    Arguments:
        a {List[int]} -- список значений а
        m {List[int]} -- список значений модулей

    Returns:
        int -- остаток
    """
    result = 0
    # Находим произведение всех модулей
    M = reduce(lambda x, y: x * y, m)
    for a_i, m_i in zip(a, m):
        M_i = M // m_i
        result += a_i * modular_inv(M_i, m_i) * M_i
    return result % M


def sylvester_pohlig_hellman_method(a: int, b: int, p: int) -> int:
    """
    Метод Сильвестра-Полига-Хеллмана для решения задачи дискретного логарифмирования.

    Arguments:
        a {int} -- первое число
        b {int} -- второе число
        p {int} -- модуль

    Returns:
        int -- число x, удовлетворяющее сравнению a^x = b (mod p)
    """
    # Находим порядок числа а по модулю p
    ord_pa = ord(a, p)
    # Находим p_i^alpha_i
    factors = factorize(ord_pa)
    # Находим mu_i = ord(a, p) / p_i^alpha_i
    mu = [ord_pa // factor for factor in factors]
    # Находим x_i
    x = [matching_method(binary_pow(a, mu_i, p), binary_pow(b, mu_i, p), p) for mu_i in mu]
    # Находим x используя китайскую теорему об остатках
    return chineese_remainder_theorem(x, factors)


def check_results(a: int, b: int, p: int, x: int) -> bool:
    """
    Проверяет является ли x решением сравнения a^x = b (mod p)

    Arguments:
        a {int} -- первое число
        b {int} -- второе число
        p {int} -- модуль
        x {int} -- число

    Returns:
        bool -- True, если x решение сравнения a^x = b (mod p)
    """
    return binary_pow(a, x, p) == b % p


def find_result_and_check(method: Callable, a: int, b: int, p: int) -> int:
    """
    Находит х используя `method`. Проверяет является ли х решением сравнения a^x = b (mod p).
    Выводит всю информацию в консоль.

    Arguments:
        method {Callable} -- метод для поиска решения
        a {int} -- первое число
        b {int} -- второе число
        p {int} -- модуль

    Returns:
        int -- число x, удовлетворяющее сравнению a^x = b (mod p)
    """
    x = method(a, b, p)
    print(f"Найденный х: {x}")
    print(f"{a} ^ {x} = {binary_pow(a, x, p)}", end="")
    if check_results(a, b, p, x):
        print(f" = {b} (mod {p})")
    else:
        print(f" != {b} (mod {p})")


if __name__ == "__main__":
    # Вариант 4
    VARIANT_NUMBERS = (3, 250, 1307)
    print('Вариант 4')
    print("a = {} b = {} p = {}".format(*VARIANT_NUMBERS))
    # Метод согласования
    print("Метод согласования")
    find_result_and_check(matching_method, *VARIANT_NUMBERS)
    # Метод Сильвестра-Полига-Хеллмана
    print("Метод Сильвестра-Полига-Хеллмана")
    find_result_and_check(sylvester_pohlig_hellman_method, *VARIANT_NUMBERS)