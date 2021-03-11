import sys
import threading

# Thanks Bill Gates
threading.stack_size(67108864)  # 64MB stack
sys.setrecursionlimit(2 ** 20)

def ex1():
    def exercise1LinearSearch(arr, to_find):
        n = len(arr)
        for i in range(n):
            print(*arr)
            printlen = len(' '.join([str(e) for e in arr[:i + 1]])) - 1
            print(' ' * printlen + '^')
            if arr[i] == to_find:
                print(f'Found {to_find}. The index is {i}')
                return i
        print(f'(╯°□°) ╯ ┻━┻ There is no {to_find} in array...')
        return -1

    def exercise1BinarySearch(arr, to_find):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            print(*arr)
            leftlen = len(' '.join([str(e) for e in arr[:left + 1]])) - 1
            midlen = len(' '.join([str(e) for e in arr[left + 1:mid + 1]]))
            rightlen = len(' '.join([str(e) for e in arr[mid + 1:right + 1]]))
            print(' ' * leftlen + '^' + ' ' * midlen + '^' + ' ' * rightlen + '^')
            print(' ' * leftlen + 'l' + ' ' * midlen + 'm' + ' ' * rightlen + 'r')

            if arr[mid] < to_find:
                left = mid + 1
            elif arr[mid] > to_find:
                right = mid - 1
            else:
                print(f'Found {to_find}. The index is {mid}')
                return mid

        print(f'(╯°□°) ╯ ┻━┻ There is no {to_find} in array...')
        return -1

    print('a)')
    exercise1LinearSearch([-7, 1, 3, 3, 4, 7, 11, 13], 7)  # a
    print('\nb)')
    exercise1BinarySearch([-7, 2, 2, 3, 4, 7, 8, 11, 13], 8)  # b
    print('\nc)')
    exercise1BinarySearch([-7, 1, 2, 3, 5, 7, 10, 13], 8)  # c


def ex2():
    def exercise2(arr, to_find):
        left = 0
        right = len(arr)
        while left < right:
            middle = (left + right) // 2
            if arr[middle] == to_find:
                return middle
            elif arr[middle] < to_find:
                left = middle + 1
            else:
                right = middle

        return -left - 1

    tests = [
        ([1, 3, 7, 9, 11], 3),
        ([1, 3, 7, 9, 11], 0),
        ([2, 4, 5, 6, 7, 10, 10, 10,
          12, 18, 21, 22, 40, 53, 61, 82], 10),
        ([2, 4, 5, 6, 7, 10, 10, 10,
          12, 18, 21, 22, 40, 53, 61, 82], 9)
    ]

    for test in tests:
        res = exercise2(*test)
        if res >= 0:
            print(f'\nFound {test[1]}. The index is {res}')
            print(*test[0])
            printlen = len(' '.join([str(e) for e in test[0][:res + 1]])) - 1
            print(' ' * printlen + '^')
        else:
            print(
                f'\n{test[1]} could be inserted before element with index {-(res + 1)}')
            print(*test[0])
            printlen = len(' '.join([str(e)
                                     for e in test[0][:-(res + 1) + 1]])) - 1
            print(' ' * printlen + '^')
            print(f'Modified Binary Search returned: {res}')
        print('--------------------------------------------')


def ex3():
    from random import randint
    from timeit import default_timer as timer

    def betterLinearSearch(arr, n, x):
        for i in range(n):
            if arr[i] == x:
                return i
        return -1

    def sentinelLinearSearch(arr, n, x):
        last, arr[n - 1] = arr[n - 1], x
        i = 0
        while arr[i] != x:
            i += 1
        arr[n - 1] = last
        if i < n - 1 or arr[n - 1] == x:
            return i
        return -1

    def recursiveLinearSearch(arr, n, i, x):
        if i >= n:
            return -1
        elif arr[i] == x:
            return i
        else:
            return recursiveLinearSearch(arr, n, i + 1, x)

    def test(testLength):
        def generateArrayandElement(n):
            array = []
            for _ in range(n):
                array.append(randint(0, 10000))
            element = randint(0, 10000)
            return array, element

        print(f"For n = {testLength}")
        arr, x = generateArrayandElement(testLength)
        n = len(arr)
        start = timer()
        bls_res = betterLinearSearch(arr, n, x)
        betterLinearSearchTime = timer() - start
        print(" Better linear search res:", bls_res)
        start = timer()
        sls_res = sentinelLinearSearch(arr, n, x)
        sentinelLinearSearchTime = timer() - start
        print(" Sentinel Linear Search:", sls_res)
        start = timer()
        rls_res = recursiveLinearSearch(arr, n, 0, x)
        recursiveLinearSearchTime = timer() - start
        print(" Recursive linear search res:", rls_res)

        return betterLinearSearchTime, sentinelLinearSearchTime, recursiveLinearSearchTime

    tests = [[], [], []]
    for i in [500, 1000, 5000]:
        temp = test(i)
        for j in range(3):
            tests[j].append(temp[j])
    names = [
        "Better-Linear-Search    ",
        "Sentinel-Linear-Search  ",
        "Recursive-Linear-Search "
    ]

    print(' ' * max(map(len, names)) + '|' + ' ' * 10 +
          'Time depending on the input data' + ' ' * 11 + '|')
    print(' ' * max(map(len, names)) + '|' + ' ' * 6 +
          'n=500' + ' ' * 6 + '|', end='')
    print(' ' * 6 + 'n=1000' + ' ' * 5 + '|', end='')
    print(' ' * 6 + 'n=5000' + ' ' * 5 + '|',)
    for i in range(len(tests)):
        t = list(map("{:.15f}".format, tests[i]))
        print(f"{names[i]}|{t[0]}|{t[1]}|{t[2]}|")


print('\nExercise 1\n')
ex1()
print('\nExercise 2')
ex2()
print('\nExercise 3\n')
thread = threading.Thread(target=ex3)
thread.start()
