from typing import List, Tuple
from random import choice, randint
from math import gcd


def find_all_prime_numbers_in_range(start: int, finish: int) -> List:
    """
    Находит все простые числа на заданном промежутке `[start, finish]`.
    Для нахождения простых чисел используется модифицированное Решето Эратосфена.

    Arguments:
        start {int} -- начало промежутка
        finish {int} -- конец промежутка

    Returns:
        List -- список простых чисел
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


def get_random_prime_number_in_range(start: int, finish: int) -> int:
    """
    Возвращает случайное простое число из промежутка.

    Arguments:
        start {int} -- начало промежутка
        finish {int} -- конец промежутка

    Returns:
        int -- случайное простое число
    """
    # находим все простые числа на интервале
    primes = find_all_prime_numbers_in_range(start, finish)
    # выбираем случайное простое число из найденных
    return choice(primes)


def find_all_coprimes_in_range(start: int, finish: int, number: int) -> List[int]:
    """
    Находит все числа на промежутке `[start, finish]` взаимно простые с `number`.

    Arguments:
        start {int} -- начало промежутка
        finish {int} -- конец промежутка

    Returns:
        List[int] - все числа, взаимно простые с `number`.
    """
    return [i for i in range(start, finish + 1) if gcd(number, i) == 1]


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


def get_key_pair(p: int, coprimes: List[int]) -> Tuple[int, int]:
    """
    Находит первый и второй ключи.

    Arguments:
        coprimes {List[int]} -- все простые числа на промежутке `[1, p - 1]`.
        p {int} -- простое число.

    Returns:
        Tuple[int, int] -- первый и второй ключи.
    """
    # выбираем первый ключ из простых чисел
    key_1 = choice(coprimes)
    key_2 = modular_inv(key_1, p - 1)
    return key_1, key_2


def prepare_keys(p: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Генерирует ключи для Криптосистемы без передачи ключей.

    Arguments:
        p {int} -- простое число

    Returns:
        Tuple[Tuple[int, int], Tuple[int, int]] -- пара из двух пар ключей.
    """
    # находим все числа большие 0, меньшие p - 1 и взаимно простые с p - 1
    coprimes = find_all_coprimes_in_range(1, p - 2, p - 1)
    # находим первый и второй ключи для первого и второго Абонента
    a, alpha = get_key_pair(p, coprimes)
    b, beta = get_key_pair(p, coprimes)
    return (a, alpha), (b, beta)


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


def step_1(m: int, a: int, p: int) -> int:
    """
    Абонент A составляет сообщение для абонента B.

    Arguments:
        m {int} -- сообщение
        a {int} -- первый ключ абонента A
        p {int} -- простое число

    Returns:
        int -- зашифрованное сообщение
    """
    m_1 = binary_pow(m, a, p)
    return m_1


def step_2(m_1: int, b: int, p: int) -> int:
    """
    Абонент B шифрует сообщение m_1 ключом b.

    Arguments:
        m_1 {int} -- зашифрованное сообщение
        b {int} -- первый ключ абонента B
        p {int} -- простое число

    Returns:
        int -- зашифрованное сообщение
    """
    m_2 = binary_pow(m_1, b, p)
    return m_2


def step_3(m_2: int, alpha: int, p: int) -> int:
    """
    Абонент A шифрует сообщение m_2 ключом alpha.

    Arguments:
        m_2 {int} -- зашифрованное сообщение
        alpha {int} -- второй ключ абонента A
        p {int} -- простое число

    Returns:
        int -- зашифрованное сообщение
    """
    m_3 = binary_pow(m_2, alpha, p)
    return m_3


def step_4(m_3: int, beta: int, p: int) -> int:
    """
    Абонент B расшифровывает сообщение m_3 ключом beta.

    Arguments:
        m_3 {int} -- зашифрованное сообщение
        beta {int} -- второй ключ абонента B
        p {int} -- простое число

    Returns:
        int -- расшифрованное сообщение
    """
    m_4 = binary_pow(m_3, beta, p)
    return m_4


def task(a: int, b: int) -> None:
    """
    Функция выполняющая задание.

    Arguments:
        a {int} -- начало промежутка
        b {int} -- конец промежутка

    Returns:
        None
    """
    # 1. Используя простое число из заданного промежутка [a,b] в качестве модуля,
    #    приготовьте ключи в системе «без передачи ключей».
    p = get_random_prime_number_in_range(a, b)
    print(f'Простое число: {p}')
    (a, alpha), (b, beta) = prepare_keys(p)
    print(f'Ключи абонента A: {a}, {alpha}')
    print(f'Ключи абонента B: {b}, {beta}')
    # 2. Возьмите в качестве сообщения число из заданного промежутка,
    #    зашифруйте с помощью одного из ваших ключей и передайте напарнику.
    #    Выполните подтверждение (шифрование) при запросе напарника.
    # Выбираем случайное m в промежутке [a, p)
    m = randint(a, p - 1)
    print(f"Выбранное сообщение: {m}")
    # Шифруем m и передаем напарнику
    m_1 = step_1(m, a, p)
    print(f"Сообщение Зашифрованное первым ключом: {m_1}")
    # 3. Получите зашифрованное сообщение от напарника. Начните процесс дешифрования.
    #    Отправьте запрос о подтверждении. При получении вскройте сообщение.
    #    Сверьте полученные данные с напарником.
    # Получаем зашифрованное сообщение от напарника
    m_2 = step_2(m_1, b, p)
    print(f"Сообщение зашифрованное первым ключом напарника: {m_2}")
    # Начинаем дешифрование
    m_3 = step_3(m_2, alpha, p)
    print(f"Сообщение зашифрованное вторым ключом: {m_3}")
    # Дешифруем и подтверждаем
    m_4 = step_4(m_3, beta, p)
    print(f"Сообщение дешифрованное вторым ключом напарника: {m_4}")
    # Сверяем полученные данные с напарником
    if m_4 == m:
        print(f'm = {m} и m_4 = {m_4} совпадают')
    else:
        print(f'm = {m} и m_4 = {m_4} не совпадают')


if __name__ == "__main__":
    # Значения для 4 варианта: (a, b)
    VARIANT_VALUES = (20, 70)
    # Запуск задания
    task(*VARIANT_VALUES)
