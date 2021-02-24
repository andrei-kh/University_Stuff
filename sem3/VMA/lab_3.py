import numpy as np

C = np.array([[16., 3.],
              [7., -11.]])
# initialize the RHS vector
b = np.array([11., 13.])

print("System of equations:")
for i in range(C.shape[0]):
    row = ["{0:3g}*x{1}".format(C[i, j], j + 1) for j in range(C.shape[1])]
    print(" [{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

x = np.zeros_like(b)
normal = (-np.linalg.inv(np.tril(C))).dot(np.triu(C) - np.diag(np.diag(C)))
print('Matrix A:\n', normal)
normal = np.sum(np.absolute(normal), axis=1).max()
print('Normal:', normal)
it_count = 0
while(True):
    it_count += 1
    x_new = np.zeros_like(x)
    print("Iteration {0}: {1}".format(it_count, x))
    for i in range(C.shape[0]):
        s1 = np.dot(C[i, :i], x_new[:i])
        s2 = np.dot(C[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / C[i, i]
    if np.allclose(x, x_new, rtol=1e-8):
        break
    x = x_new

print("Solution: {0}".format(x))
error = np.dot(C, x) - b
print("Error: {0}".format(error))
