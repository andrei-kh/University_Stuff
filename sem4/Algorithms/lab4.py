from sys import maxsize
import matplotlib.pyplot as plt
from os import system
# from numba import njit
# import warnings
# warnings.filterwarnings('ignore')
system('cls')

# @njit
def countingSort(array, n, m):
    def rearrange(A, less, n, m):
        next = []
        for j in range(m):
            next.append(less[j] + 1)

        k = 0
        B = [-1 for _ in range(n)]
        for i in range(0, n):
            key = A[i]
            index = next[key]
            B[index - 1] = A[i]
            next[key] += 1

            if SHOW_PROGRESS_BAR:
                if i >= k * (n // 100):
                    progressBar(i, n, "\tRearrange progress:        ", dec=2, length=100)
                    k += 1
                if i == n - 1:
                    progressBar(n, n, "\tRearrange progress:        ", dec=2, length=100, end='\n')

        return B

    def countKeysLess(equal, m):
        less = [0]
        k = 0
        for j in range(1, m):
            less.append(less[j - 1] + equal[j - 1])

            if SHOW_PROGRESS_BAR:
                if j >= k * (m // 100):
                    progressBar(j, m, "\tCount Keys Less progress:  ", dec=2, length=100)
                    k += 1
                if j == m - 1:
                    progressBar(m, m, "\tCount Keys Less progress:  ", dec=2, length=100, end='\n')

        return less

    def countKeysEqual(A, n, m):
        equal = [0 for _ in range(m)]

        k = 0
        for i in range(n):
            key = A[i]
            equal[key] += 1

            if SHOW_PROGRESS_BAR:
                if i >= k * (n // 100):
                    progressBar(i, n, "\tCount Keys Equal progress: ", dec=2, length=100)
                    k += 1
                if i == n - 1:
                    progressBar(n, n, "\tCount Keys Equal progress: ", dec=2, length=100, end='\n')

        return equal

    equal = countKeysEqual(array, n, m)
    less = countKeysLess(equal, m)
    B = rearrange(array, less, n, m)
    return B


# @njit
def insertionSort(array, n):
    k = 0
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

        if SHOW_PROGRESS_BAR:
            if i >= k * (n // 100):
                progressBar(i, n, "\tInsertion Sort progress:   ", dec=2, length=100)
                k += 1
            if i == n - 1:
                progressBar(n, n, "\tInsertion Sort progress:   ", dec=2, length=100, end='\n')


# @njit
def mergeSort(array, p, r, ti=None, k=None):
    def merge(A, p, q, r):
        B = [A[i] for i in range(p, q + 1)]
        C = [A[i] for i in range(q + 1, r + 1)]
        B.append(maxsize)
        C.append(maxsize)
        i, j = 0, 0
        for k in range(p, r + 1):
            if B[i] <= C[j]:
                A[k] = B[i]
                i += 1
            elif B[i] >= C[j]:
                A[k] = C[j]
                j += 1
    if ti is None:
        ti = [0]

    if k is None:
        k = [0]

    if p >= r:
        return

    if SHOW_PROGRESS_BAR:
        ti[0] += 1
        if ti[0] >= k[0] * (len(array) // 100):
            progressBar(ti[0], len(array), "\tMerge Sort progress:       ", dec=2, length=100)
            k[0] += 1

        if ti[0] == len(array) - 1:
            progressBar(len(array), len(array), "\tMerge Sort progress:       ", dec=2, length=100, end='\n')

    q = (p + r) // 2
    mergeSort(array, p, q, ti, k)
    mergeSort(array, q + 1, r, ti, k)
    merge(array, p, q, r)


def progressBar(citer, maxiter=100, prefix='', dec=1, length=100, symbol='■', end=''):
    p = citer // (maxiter // length)
    print(f"\r{prefix}|{symbol * (p // dec) + '-' * (length // dec  - p // dec)}|{(100 // length) * p}%", end=end)


def test(testLength):
    from random import randint
    from timeit import default_timer as timer

    def generateArray(n):
        array = []
        for _ in range(n):
            array.append(randint(0, 100000))
        return array, array.copy(), array.copy()

    testResults = []
    print(f"[?] Tests for n = {testLength} are starting\n")

    arr1, arr2, arr3 = generateArray(testLength)
    n = len(arr1)
    teststart = timer()
    start = timer()
    cnt_sort_res = countingSort(arr1, n, max(arr1) + 1)
    testResults.append(timer() - start)
    print(f"   [-]Counting sort is done for n = {n}\n")

    start = timer()
    insertionSort(arr2, n)
    testResults.append(timer() - start)
    print(f"   [-]Insertion sort is done for n = {n}\n")

    start = timer()
    mergeSort(arr3, 0, len(arr3) - 1)
    testResults.append(timer() - start)
    print(f"   [-]Merge sort is done for n = {n}\n")

    sarr = sorted(arr1)
    if cnt_sort_res != sarr:
        raise ValueError("Invalid Count Sort")

    if arr2 != sarr:
        raise ValueError("Invalid Insertion Sort")

    if arr3 != sarr:
        raise ValueError("Invalid Merge Sort")

    print(f"[+]Tests for n = {testLength} are completed in {format(timer() - teststart, '.5f')} sec")
    print("===========================================================================================")
    return testResults


print(' ' * 43 + 'Lab 4' + ' ' * 43)
print("=" * 91)

TEST_LENGHTH = 50000
TEST_QUANTITY = 20
SAVE_PLOT = False
SHOW_PLOT = True
SHOW_PROGRESS_BAR = True

names = [
    "Counting Sort",
    "Insertion Sort",
    "MergeSort",
]
tests = [[], [], []]
ranges = []
for i in range(1, TEST_QUANTITY + 1):
    ranges.append(i * TEST_LENGHTH)
    temp = test(ranges[-1])
    for j in range(len(temp)):
        tests[j].append(temp[j])


markers = ['s', 'o', 'D']
fig = plt.figure(num=None, figsize=(16, 9))
for i in range(len(names)):
    plt.plot(ranges, tests[i], marker=markers[i], label=names[i])
plt.ylabel('sec')
plt.xlabel('n')
plt.grid(which='major', axis='both', linestyle='--')
plt.xticks(ranges, list(map(str, ranges)))
plt.legend(loc='upper left')
if SAVE_PLOT:
    plt.savefig('lab4plot.png', bbox_inches='tight', dpi=300)
if SHOW_PLOT:
    plt.show()
