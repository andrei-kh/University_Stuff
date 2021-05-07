from math import sqrt


def check_prime(num):
    if num == 0:
        return False

    if num == 1:
        return True

    for i in range(2, int(sqrt(num) + 2)):
        if num % i == 0:
            return False

    return True


list_ = [0, 1, 12, 23, 27, 31, 41, 47, 103, 108, 113, 137, 138, 139]
res = [str(n) for n in list_ if check_prime(n)]

print(";".join(res))