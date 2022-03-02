from sympy import parse_expr, lambdify

# формулы http://mathhelpplanet.com/static.php?p=chislennyye-metody-resheniya-krayevykh-zadach


def print_table(table, headers, e='.3f'):
    new_table = [headers]
    max_h_len = [len(_) for _ in headers]
    for i in range(len(table)):
        new_table.append([])
        for j in range(len(table[0])):
            if isinstance(table[i][j], str):
                new_table[-1].append(table[i][j])
            elif isinstance(table[i][j], int):
                new_table[-1].append(str(table[i][j]))
            else:
                new_table[-1].append(str(format(table[i][j], e)))

            max_h_len[j] = max(max_h_len[j], len(new_table[-1][j]))

    headers_str = "| "
    for i in range(len(new_table[0])):
        half1 = (max_h_len[i] - len(new_table[0][i])) // 2
        half2 = max_h_len[i] - half1 - len(new_table[0][i])
        headers_str += ' ' * half2 + new_table[0][i] + ' ' * half1 + ' | '
    print(headers_str)
    print('-' * (len(headers_str) - 1))

    for r in new_table[1:]:
        print('| ', end='')
        for i in range(len(r)):
            half1 = (max_h_len[i] - len(r[i])) // 2
            half2 = max_h_len[i] - half1 - len(r[i])
            print(' ' * half2 + r[i] + ' ' * half1, end=' | ')
        print()


# start params
h = 0.1

alpha0 = 1
alpha1 = 1
beta0 = 0
beta1 = 0

A = B = 0

a = 0
b = 0.4

p = parse_expr("1 + x**3")
q = parse_expr("x ** 2 - 1")
f = parse_expr("exp(1 - 4.5 * x**2)")

# end params

lams = {v: lambdify(list(v.free_symbols), v) for v in [p, q, f]}

n = int((b - a) / h) + 1
x = [a + h * i for i in range(n)]

u1 = [- beta0 / alpha0]
u2 = [- A / alpha0]

table = []
for i in range(n):
    fu1 = -u1[i] * (u1[i] * lams[q](x[i]) - lams[p](x[i])) + 1
    u1.append(u1[i] + h * fu1)
    fu2 = -u1[i] * (u2[i] * lams[q](x[i]) + lams[f](x[i]))
    u2.append(u2[i] + h * fu2)
    table.append([x[i], fu1, fu2])

print_table(table, ['x', 'f(x, u1)', 'f(x, u2)'])
print()

y_b = (B * u1[-1] + beta1 * u2[-1]) / (beta1 + alpha1 * u1[-1])
y = [None for _ in range(n - 1)] + [y_b]

for i in range(n - 1, 0, -1):
    fy = (y[i] - u2[i]) / u1[i]
    y[i - 1] = y[i] - h * fy

table = [[x[i], u1[i], u2[i], y[i]] for i in range(n)]
print_table(table, ['x', 'u1', 'u2', 'y'])
