from itertools import product
from itertools import groupby
from itertools import combinations_with_replacement
from itertools import combinations
from itertools import permutations
import csv
from collections import Counter
from collections import defaultdict
from collections import deque

# 1


def count_colors_labels(colors_labels):
    dict_ = defaultdict(int)

    for tuples in list(dict.fromkeys(colors_labels)):
        dict_[tuples[0]] += 1

    print(dict_)


elems = [('yellow', 3), ('green', 4), ('green', 4),
         ('red', 2), ('green', 7), ('yellow', 4)]


# 2
def tail(filename, n=10):
    de = deque()
    with open(filename) as file:
        for line in (file.readlines()[-n:]):
            de.append(line.rstrip())
    return de


filename = 'test.txt'
last_lines = deque(["If you can talk with crowds and keep your virtue,",
                    "Or walk with Kings - nor lose the common touch,",
                    "If neither foes nor loving friends can hurt you,",
                    "If all men count with you, but none too much:",
                    "If you can fill the unforgiving minute",
                    "With sixty seconds' worth of distance run,",
                    "Yours is the Earth and everything that's in it,",
                    "And - which is more - you'll be a Man, my son!"])


# 3
def get_least_common(iterable_obj, n=3):
    least_common = []
    for a in Counter(iterable_obj).most_common()[:- n - 1:-1]:
        least_common.append(a[0])
    return least_common


elems = [1, 4, 3, 1, 1, 8, 9, 2, 8, 8, 9, 9]


# 4
def read_employees(filename):
    with open(filename, newline='') as csvfile:
        employee_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        employees = [' '.join(row) for row in employee_reader]
        return employees


# print(read_employees('test.csv'))


# 5
def get_permutations(s, n):
    return sorted([''.join(permutation) for permutation in permutations(s, n)])

# print(get_permutations("cat", 2))
# assert get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"]


# 6
def get_combinations(s, n):
    combinations_to_return = []
    for i in range(1, n + 1):
        combinations_to_return += sorted([''.join(comb)
                                          for comb in list(combinations(s, i))])
    return combinations_to_return

# print(get_combinations("cat", 2))
# assert get_combinations("cat", 2) == ["a", "c", "t", "at", "ca", "ct"]


# 7
def get_combinations_with_r(s, n):
    return sorted(''.join(comb) for comb in list(combinations_with_replacement(s, n)))


# print(get_combinations_with_r("cat", 2))
# assert get_combinations_with_r("cat", 2) == ["aa", "at", "ca", "cc", "ct", "tt"]


# 8
def compress_string(s):
    return [(len(list(group)), int(key)) for key, group in groupby(s)]


# print(compress_string('1222311'))
# assert compress_string('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)]


# 9
def maximize(lists, m):
    pow2lists = []
    for list_ in lists:
        pow2lists.append(map(lambda x: x**2, list_))
    return max(map(lambda x: sum(x) % m, product(*pow2lists)))


lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
# print(maximize(lists, m=1000))
# assert maximize(lists, m=1000) == 206


# 10
def split(lists):
    return [int(x) for x in lists.split(',')]


# str_list = "1, 2, 45, 555,5,5,23,4234"
# print(split(str_list))
# assert split(str_list) == [1, 2, 45, 555, 5, 5, 23, 4234]
