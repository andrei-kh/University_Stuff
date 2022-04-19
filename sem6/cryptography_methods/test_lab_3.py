from typing import Tuple, List
import pytest
from math import gcd, sqrt
from random import randint
from lab_3 import factorize, check_results, sylvester_pohlig_hellman_method, matching_method, ord


def get_test_values(number_of_tests: int) -> List[Tuple[int, int, int]]:
    """
    Получает набор тестовых значений для проверки алгоритма.

    Arguments:
        number_of_tests {int} -- кол-во тестовых значений

    Returns:
        List[Tuple[int, int, int]] -- список тестовых значений
    """
    test_values = []
    for _ in range(number_of_tests):
        p = randint(10, 10000)
        a = randint(1, 10000)
        b = randint(1, 10000)
        test_values.append((a, b, p))
    return test_values


def is_prime(n: int) -> bool:
    """
    Проверяет, является ли число простым.

    Arguments:
        n {int} -- проверяемое число

    Returns:
        bool -- True, если число простое, иначе False
    """
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def check_values(a: int, b: int, p: int) -> bool:
    """
    Проверяет значения параметров алгоритма.

    Arguments:
        a {int} -- первое число
        b {int} -- второе число
        p {int} -- простое число

    Returns:
        bool -- True, если значения прошли проверку, иначе False
    """
    return gcd(a, p) == 1 and gcd(b, p) == 1 and p != 2 and is_prime(p)


@pytest.mark.parametrize("a, b, p", get_test_values(1000))
def test_sylvester_pohlig_hellman_method(a, b, p):
    """
    Тестирует работу метода Сильвестра-Поллига-Хеллмана.
    """
    # Проверяем значения на соответствие условиям
    if not check_values(a, b, p) or len(factorize(ord(a, p))) == 1:
        try:
            x = sylvester_pohlig_hellman_method(a, b, p)
            # Алгоритм может найти решение и не для простых чисел
            # Проверяем, в данном случае решение найдено верно
            assert check_results(a, b, p, x)
        except TypeError:
            assert True
    else:
        # Если значения подходят под условия и есть решение сравнения, то проверяем, что оно найдено верно
        x = sylvester_pohlig_hellman_method(a, b, p)
        if x is not None:
            assert check_results(a, b, p, x)


@pytest.mark.parametrize("a, b, p", get_test_values(1000))
def test_matching_method(a, b, p):
    """
    Тестирует работу метода согласования.
    """
    # Проверяем значения на соответствие условиям
    if not check_values(a, b, p):
        try:
            x = matching_method(a, b, p)
            # Алгоритм может найти решение и не для простых чисел
            # Проверяем, в данном случае решение найдено верно
            assert check_results(a, b, p, x)
        except TypeError:
            pass
    else:
        # Если значения подходят под условия и есть решение сравнения, то проверяем, что оно найдено верно
        x = matching_method(a, b, p)
        if x is not None:
            assert check_results(a, b, p, x)
        else:
            print(a, b, p)
