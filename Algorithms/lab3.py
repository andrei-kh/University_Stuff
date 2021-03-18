from random import randint
from sys import argv


# Задание 1
def ex1() -> None:
    from math import log2
    print("\nExercise 1\n")
    print("Algorithm A: T(n) = 5 * T(n / 2) + Θ(n^1)")
    print("\tMaster theorem (case 1):")
    print(f"\t1 < log2(5) = {log2(5)}")
    print("\tAnswer: T(n) = Θ(n^log2(5))")
    print()
    print("Algorithm B: T(n) = 2 * T(n - 1) + Θ(1)")
    print("\tMaster theorem dosen't fit here.")
    print("\tWe can observe that recursion would divide problem 2^n - 1 times")
    print("\tand combine resulting subproblems in constant time:")
    print("\tAnswer: T(n) = Θ(2^n - 1) = Θ(2^n)")
    print()
    print("Algorithm C: T(n) = 9 * T(n / 3) + Θ(n^2)")
    print("\tNote: If you really put n=3 T(n) = Θ(1), so i suppose that size is n / 3")
    print("\tWe can use Master Theorem (case 2):")
    print("\tΘ(n^2 * log(n)^0) = Θ(n^2), so")
    print("\tT(n) = Θ(n^2 * log(n))")
    print()
    print("The fastest algorithm is C, so i would choose it.")


def merge2Arrays(arr1, arr2) -> list:
    res = []

    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    res += arr1[i:]
    res += arr2[j:]

    return res


def ex2() -> None:
    def generateSortedArrays(n, k, min_v=-100, max_v=100) -> list:
        arrays = []
        for i in range(k):
            array = []
            for i in range(n):
                array.append(randint(min_v, max_v))
            arrays.append(sorted(array))
        return arrays

    # Задание 2 а)
    def ex2a(arrays) -> list:
        res = merge2Arrays(arrays[0], arrays[1])
        for i in range(2, len(arrays)):
            res = merge2Arrays(res, arrays[i])
        return res

    # Задание 2 б)
    def ex2b(i, j, arrays) -> list:
        if i == j:
            return arrays[i]
        if j - i == 1:
            return merge2Arrays(arrays[i], arrays[j])
        arr1 = ex2b(i, (i + j) // 2, arrays)
        arr2 = ex2b((i + j) // 2 + 1, j, arrays)
        return merge2Arrays(arr1, arr2)

    print("\nExercise 2\n")
    print("Input n and k: ", end='')
    n, k = map(int, input().split())
    arrays = generateSortedArrays(n, k)
    print("\nArrays before merging:")
    print(*arrays)
    print("\nArrays after merging:")
    print("a)\n===================")
    print(ex2a(arrays), end='\n\n')
    print("b)\n===================")
    print(ex2b(0, k - 1, arrays), end='\n\n')


# Задание 3
def ex3() -> None:
    def merge_sort(array):
        if len(array) < 20:
            return sorted(array)

        mid = len(array) // 2
        P = merge_sort(array[:mid])
        R = merge_sort(array[mid:])
        return merge2Arrays(P, R)

    print("\nExercise 3\n")
    print("Input strings: ", end='')
    array = input().split()
    print("\nArray of strigs before sort:", end='\n\t')
    print(array)
    print("\nArray of strings after sort:", end='\n\t')
    print(merge_sort(array))


# Задание 4
def ex4() -> None:
    def generateArray(n, m) -> list:
        res = []
        for _ in range(n):
            res.append(randint(0, m - 1))

        return res

    def rearrange(A, n, m) -> list:
        equal = countKeysEqual(A, n, m)
        # print(equal)
        less = countKeyLess(equal, m)
        # print(less)
        next = []
        for j in range(m):
            next.append(less[j] + 1)

        B = [None for _ in range(n)]
        for i in range(0, n):
            key = A[i]
            index = next[key]
            B[index - 1] = A[i]
            next[key] += 1

        return B

    def countKeyLess(equal, m) -> list:
        less = [0]
        for j in range(1, m):
            less.append(less[j - 1] + equal[j - 1])

        return less

    def countKeysEqual(A, n, m) -> list:
        equal = [0 for _ in range(m)]

        for i in range(n):
            key = A[i]
            equal[key] += 1

        return equal

    print("\nExercise 4\n")
    print("Input m and n: ", end='')
    n, m = map(int, input().split())
    arr = generateArray(n, m)
    print("\nArray before sort:", end='\n\t')
    print(arr)
    print("\nArray after sort:", end='\n\t')
    print(rearrange(arr, n, m))


if __name__ == "__main__":
    if len(argv) == 1:
        ex1()
        ex2()
        ex3()
        ex4()
    else:
        if argv.count('1') >= 1:
            ex1()
        if argv.count('2') >= 1:
            ex2()
        if argv.count('3') >= 1:
            ex3()
        if argv.count('4') >= 1:
            ex4()
