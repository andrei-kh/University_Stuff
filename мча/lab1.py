from math import exp, sin

from utils import print_table
import matplotlib.pyplot as plt

def func(t, u):
    return -2 * t * u + t * exp(-t * t) * sin(t)


def euler_method(f, h, t0=0, T=1, u0=1):
    n = int((T - t0) / h)

    t = [t0 + i * h for i in range(0, n + 1)]
    u = [u0]

    for i in range(n):
        ui_new = u[i] + h * f(t[i], u[i])

        u.append(ui_new)

    return u, t


u1, t1 = euler_method(func, 0.1)
u2, t2 = euler_method(func, 0.05)

table = []

for i in range(max(len(u1), len(u2))):
    try:
        table.append([t1[i], t2[i], u1[i], u2[i]])
    except IndexError:
        table.append(['-', t2[i], '-', u2[i]])

print_table(table, ['t (h = 0.1)', 't (h = 0.05)', 'u (h=0.1)', 'u (h=0.05)'])

fig, ax = plt.subplots()
ax.set_title("Явный метод Эйлера")

p1 = plt.plot(t1, u1, marker='o', color='r', label='h=0.1')
p2 = plt.plot(t2, u2, marker='o', color='b', label='h=0.05')

plt.legend()
plt.show()
