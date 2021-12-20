def extended_gcd_r(a, b):
    if b == 0:
        return a, 1, 0

    d, x, y = extended_gcd_r(b, a % b)
    return d, y, x - y * (a // b)


def modinv(a, m):
    g, x, y = extended_gcd_r(a, m)
    if g != 1:
        raise ValueError

    return x % m


class ModMatrix:
    def __init__(self, array: list, mod) -> None:
        self.mod = mod
        self.array = array
        self.apply_mod()

    def apply_mod(self):
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                self.array[i][j] %= self.mod

    def __det_recur(self, A, mul):
        width = len(A)

        if width == 1:
            return mul * A[0][0]
        else:
            sign = -1
            ans = 0
            for i in range(width):
                m = []
                for j in range(1, width):
                    buff = []
                    for k in range(width):
                        if k != i:
                            buff.append(A[j][k])
                    m.append(buff)
                sign *= -1
                ans += mul * self.__det_recur(m, sign * A[0][i])

        return ans

    def det(self):
        return self.__det_recur(self.array, 1) % self.mod

    def __mul__(self, other):
        mul = [[0 for _ in range(len(self.array[0]))] for _ in range(len(self.array))]

        for i in range(len(self.array)):
            for j in range(len(other.array[0])):
                for k in range(len(self.array[0])):
                    mul[i][j] += self.array[i][k] * other.array[k][j]
                mul[i][j] %= self.mod

        return ModMatrix(mul, self.mod)

    def get_minor(self, i, j):
        res = []

        for x in range(len(self.array)):
            if x != i:
                res.append([])
                for y in range(len(self.array[0])):
                    if x != i and y != j:
                        res[-1].append(self.array[x][y])

        return ModMatrix(res, self.mod)

    def reverse(self):
        det = self.det()
        det = modinv(det, self.mod)

        res = [[0 for _ in range(len(self.array[0]))] for _ in range(len(self.array))]

        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                minor = self.get_minor(i, j)
                res[j][i] = ((-1) ** (i + j)) * minor.det() * det % self.mod

        return ModMatrix(res, self.mod)

    def __str__(self) -> str:
        res = ""
        for row in self.array:
            res += str(row) + "\n"
        return res


def part_to_matrix(part, alph, m):
    res = []

    for i in range(m):
        res.append(alph.index(part[i]))

    return ModMatrix([res], len(alph))


def matrix_to_part(matrix, alph):
    res = ""

    for num in matrix.array[0]:
        res += alph[num]

    return res


def message_to_matrix(message, alph, m):
    res = []

    for i in range(0, len(message), m):
        res.append(part_to_matrix(message[i:i + m], alph, m))

    return res


def hill_encrypt(A, message, alph='abcdefghijklmnopqrstuvwxyz'):
    from math import gcd
    mod = len(alph)
    A = ModMatrix(A, mod)

    if gcd(A.det(), mod) != 1:
        raise ValueError

    matricies = message_to_matrix(message, alph, len(A.array[0]))

    res = ""
    for matrix in matricies:
        matrix = matrix * A
        res += matrix_to_part(matrix, alph)

    return res


print(hill_encrypt([[10, 5, 12], [3, 14, 21], [8, 9, 11]], "august"))
