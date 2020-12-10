import numpy as np


def printeps(x, acc=3):
    for val in x:
        print(format(val, f".{acc}f"), end=" ")
    print()


def jacobi(C, b, x_init, eps=1e-15, max_iterations=500):
    D = np.diag(np.diag(C))
    LU = C - D
    x = x_init
    D_inv = np.diag(1 / np.diag(D))
    normal = (-1 * D_inv).dot(LU)
    normal = np.sum(np.absolute(normal), axis=1).max()
    for i in range(max_iterations):
        x_new = np.dot(D_inv, b - np.dot(LU, x))
        if np.linalg.norm(x_new - x) < eps:
            return normal, x_new
        x = x_new
    return normal, x


tasknum = ""
b = []
C = []
res = []

while True:
    inp = input()
    if inp == 'end':
        break
    inp = list(map(int, inp.split()))
    b.append(inp.pop())
    C.append(inp)

C = np.array(C)
b = np.array(b)
res.append(jacobi(C, b, np.zeros(len(b))))

print(C.dot(res[0][1]))
for ans in res:
    print('Normal: ', ans[0])
    printeps(ans[1])
