from typing import Optional, Callable, List, Tuple
from time import perf_counter
from lab_3 import matching_method, sylvester_pohlig_hellman_method
from test_lab_3 import check_values
from random import randint


class ExecutionTimeContextManager:
    """
    Контекстный менеджер для замера времени выполнения кода.
    """

    def __init__(self) -> None:
        self.__time: Optional[float] = None

    def __enter__(self) -> 'ExecutionTimeContextManager':
        self.__time = perf_counter()
        return self

    def __exit__(self, *exc) -> None:
        self.__time = perf_counter() - self.__time

    @property
    def time(self) -> Optional[float]:
        return self.__time


def get_values(number_of_runs: int) -> List[Tuple[int, int, int]]:
    """
    Функция генерирует значения для проверки времени исполнения.
    Значения подбираются для соответствия условиям методов.

    arguments:
        number_of_runs {int} -- кол-во запусков метода

    returns:
        List[Tuple[int, int, int]] -- список значений для проверки
    """
    values = []
    for _ in range(number_of_runs):
        a, b, p = 0, 0, 0
        # Пока числа не соответствуют условиям метода
        # генерируем новые значения
        while not check_values(a, b, p):
            a, b, p = randint(1, 1000000), randint(1, 1000000), randint(1, 1000000)
        values.append((a, b, p))
    return values


def method_mean_execution_time(method: Callable, values: List[Tuple[int, int, int]]) -> float:
    """
    Вычисляет среднее время выполнения метода.

    Arguments:
        method {Callable} -- метод для выполнения
        number_of_runs {int} -- кол-во запусков метода

    Returns:
        float -- среднее время выполнения метода
    """
    total_time = 0
    # Замеряем время выполнения кода для каждого значения
    for a, b, p in values:
        with ExecutionTimeContextManager() as time_context_manager:
            method(a, b, p)
        total_time += time_context_manager.time
    # Вычисляем среднее время выполнения метода
    return total_time / len(values)


if __name__ == "__main__":
    # Генерируем случайные значения для проверки
    values = get_values(number_of_runs=100)
    matching_method_mean_execution_time = method_mean_execution_time(matching_method, values)
    print(f"Среднее время выполнения метода согласования: {matching_method_mean_execution_time:.2f} сек.")
    sylvester_pohlig_hellman_method_mean_execution_time = method_mean_execution_time(sylvester_pohlig_hellman_method, values)
    print(f"Среднее время выполнения метода Сильвестра-Поллига-Хеллмана: {sylvester_pohlig_hellman_method_mean_execution_time:.2f} сек.")