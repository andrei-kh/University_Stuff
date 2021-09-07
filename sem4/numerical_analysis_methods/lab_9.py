from math import cos, sin


class Integrate:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        self.h = (self.b - self.a) / n

    def generalizedTrapezoid(self, f):
        result = 0

        for i in range(1, self.n):
            result += f(self.a + i * self.h)

        return self.h * (f(self.a) + f(self.b)) / 2 + self.h * result

    def generalizedSimpson(self, f):
        first = 0.0
        second = 0.0

        for i in range(1, self.n + 1):
            # if i <= self.n - 1:
            first += f(self.a + 2 * i * self.h)
            second += f(self.a + self.h * (2 * i - 1))

        return (self.h / 3.0) * (f(self.a) + f(self.b) + 2.0 * first + 4.0 * second)

    def dimension(self, i):
        switcher = {
            3: [0.707107, 0, -0.707107],
            4: [0.794654, 0.187592, -0.187592, -0.794654]}
        return switcher.get(i, [])

    def chebyshev(self, f, n):
        t = self.dimension(n)
        result = 0
        if len(t) != 0:
            for i in range(n):
                x = 0.5 * ((self.b + self.a) + (self.b - self.a) * t[i])
                result += f(x)
            return result * (self.b - self.a) / n
        return -1


def main():
    for i in range(2, 12, 2):
        integrate = Integrate(1, 2, i)
        print("n =", i, ": ")
        print('\tМетод трапеции: {:.4f}'.format(integrate.generalizedTrapezoid(f)))
        print('\tМетод Симпсона: {:.6f}'.format(integrate.generalizedSimpson(f)))
    print()
    print('\tМетод Чебышивa, n=3: {:.4f}'.format(integrate.chebyshev(f, 3)))
    print('\tМетод Чебышивa, n=4: {:.4f}'.format(integrate.chebyshev(f, 4)))


def f(x):
    return (2 * cos(x) + 3 * sin(x)) / ((2 * sin(x) - 3 * cos(x))**3)


main()
