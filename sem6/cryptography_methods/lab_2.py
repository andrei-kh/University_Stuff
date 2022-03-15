from typing import List, Tuple
from random import choice, randint, sample
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


def get_random_prime_numbers_in_range(start: int, finish: int, number_of_primes: int) -> List[int]:
    """
    Возвращает несколько случайных простых чисел из промежутка.

    Arguments:
        start {int} -- начало промежутка
        finish {int} -- конец промежутка
        number_of_primes {int} -- количество простых чисел

    Returns:
        List[int] -- случайные простые числа
    """
    # находим все простые числа на интервале
    primes = find_all_prime_numbers_in_range(start, finish)
    # выбираем случайное простое число из найденных
    return sample(primes, number_of_primes)


def find_all_coprimes_in_range(start: int, finish: int, number: int) -> List[int]:
    """
    Находит все числа на промежутке `[start, finish]` взаимно простые с `number`.

    Arguments:
        start {int} -- начало промежутка
        finish {int} -- конец промежутка
        number {int} -- число

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


def get_key_pair(phi: int, coprimes: List[int]) -> Tuple[int, int]:
    """
    Находит открытый и закрытый ключ.

    Arguments:
        phi {int} -- значение функции эйлера.
        coprimes {List[int]} -- все взаимно-простые с `phi` числа на промежутке `[1, phi - 1]`.

    Returns:
        Tuple[int, int] -- открытый и закрытый ключ.
    """
    # выбираем первый ключ из простых чисел
    key_1 = choice(coprimes)
    key_2 = modular_inv(key_1, phi)
    return key_1, key_2


def prepare_keys(p1: int, p2: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Генерирует ключи для одного из абонентов в Криптосистеме с открытым ключом.

    Arguments:
        p1 {int} -- простое число
        p2 {int} -- простое число

    Returns:
        Tuple[Tuple[int, int], Tuple[int, int]] -- пара из двух пар ключей,
                                                   произведение простых чисел и
                                                   функция эйлера от данного произведения.
    """
    # находим r
    r = p1 * p2
    # находим значение функции эйлера
    phi = (p1 - 1) * (p2 - 1)
    # находим все числа большие 0, меньшие phi и взаимно простые с phi
    coprimes = find_all_coprimes_in_range(1, phi - 1, phi)
    # находим первый и второй ключи
    a, alpha = get_key_pair(phi, coprimes)
    return a, alpha, r, phi


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


def send_message(public_key: int, private_key: int, r: int, abonent_name: str):
    # Выбираем случайное m из промежутка [1, r_b]
    m = randint(1, r)
    print(f"Выбранное сообщение: {m}")
    # Шифруем m и передаем напарнику
    m_1 = binary_pow(m, public_key, r)
    print(f"Сообщение зашифрованное открытым ключом абонента {abonent_name}: {m_1}")
    # Напарник расшифровывает сообщение своим закрытым ключом
    m_2 = binary_pow(m_1, private_key, r)
    print(f"Сообщение расшифрованное закрытым ключом абонента {abonent_name}: {m_2}")
    # Проверяем что полученное сообщение равно исходному
    if m_2 == m:
        print(f"Сообщение {m_2} соответствует исходному {m}")
    else:
        print(f"Сообщение {m_2} не соответствует исходному {m}")


def task(a: int, b: int) -> None:
    """
    Функция выполняющая задание.

    Arguments:
        a {int} -- начало промежутка
        b {int} -- конец промежутка

    Returns:
        None
    """
    # 1. Используя простые числа из заданного промежутка [a, b], создайте свой
    #    электронный адрес и ключи для работы в системе «с открытым ключом».
    #    Передайте свой адрес и ключ напарнику. Получите у него адрес и ключ.
    p1, p2 = get_random_prime_numbers_in_range(a, b, 2)
    print(f'Первое простое число для абонента А: {p1}')
    print(f'Второе простое число для абонента А: {p2}')
    q1, q2 = get_random_prime_numbers_in_range(a, b, 2)
    print(f'Первое простое число для абонента B: {q1}')
    print(f'Второе простое число для абонента B: {q2}')
    a, alpha, r_a, phi_r_a = prepare_keys(p1, p2)
    b, beta, r_b, phi_r_b = prepare_keys(q1, q2)
    print(f'Ключи абонента A: {a}, {alpha}')
    print(f"r_a = {r_a}, phi_r_a = {phi_r_a}")
    print(f'Ключи абонента B: {b}, {beta}')
    print(f"r_b = {r_b}, phi_r_b = {phi_r_b}")
    # 2. Возьмите в качестве сообщения число m, не превосходящее адрес (модуль) напарника,
    #    зашифруйте с помощью открытого ключа напарника и передайте напарнику.
    # 3. Получите сообщение от напарника, дешифруйте его.
    #    В качестве проверки отошлите полученное сообщение напарнику,
    #    используя его адрес и ключ.
    # 4. Получите ответ на ваше первое сообщение и сравните с ним.
    #    Сверьте полученные данные с напарником.
    # Сообщение шифрует абонент А
    print("Шифрование сообщения абонентом А:")
    send_message(b, beta, r_b, 'B')
    # Сообщение шифрует абонент В
    print("Шифрование сообщения абонентом В:")
    send_message(a, alpha, r_a, 'A')


if __name__ == "__main__":
    # Значения для 4 варианта: (a, b)
    VARIANT_VALUES = (20, 70)
    # Запуск задания
    task(*VARIANT_VALUES)
