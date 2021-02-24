import cv2
import numpy as np
import matplotlib.pyplot as plt
# numpy
'''
vector = (np.arange(10) == 4) * 1
print(vector)
vector = np.zeros(10, dtype=int)
vector[4] = 1
print(vector)
vector = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
print(vector)

matrix = np.arange(9).reshape(3, 3)
print(matrix)

vector = np.array([1, 2, 0, 0, 4, 0])
indexes = np.nonzero(vector)
print(*indexes)
print(vector[indexes])

matrix = np.identity(3, dtype=int)
print(matrix)

array = np.random.randint(0, 1000, size=(10, 10, 10))
print(array)

checkerboard = np.indices((8, 8)).sum(axis=0) % 2
print(checkerboard)

matrixa = np.random.randint(0, 10, size=(5, 3))
print(matrixa)
matrixb = np.random.randint(0, 10, size=(3, 2))
print(matrixb)
print(np.matmul(matrixa, matrixb))

print(np.zeros((9, 9), dtype=int) + np.arange(0, 9))

vector = np.random.randint(0, 100, size=1000)
print(vector)
print(np.mean(vector))
'''

# matplotlib
'''
xcoords = np.random.randint(1, 1001, size=100)
xcoords = np.sort(xcoords, 0)
ycoords = np.random.randint(1, 1001, size=100)
plt.plot(xcoords, ycoords)
plt.show()
'''
'''
x = np.linspace(-1000 * np.pi, 1000 * np.pi, 1000)

Tx = np.sin(x)
Px = x ** 2 - 15 * x + 20

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, Px * Tx, 'g')
plt.show()
'''
'''
x = np.linspace(-1000 * np.pi, 1000 * np.pi, 1000)

Tx = np.sin(x)
Px = x ** 2 - 15 * x + 20

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xlabel('x', fontsize=20, labelpad=100)
plt.ylabel('y', fontsize=20, labelpad=100)
plt.title('graph')
plt.plot(x, Px * Tx, 'g', label='T(x) = sin(x)\nP(x) = x^2 - 15x + 20\ny = T(x)P(X)')
plt.legend(loc='upper left')
plt.show()
'''
'''
x = np.linspace(-1000 * np.pi, 1000 * np.pi, 1000)

Tx = np.sin(x)
Px = x ** 2 - 15 * x + 20

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xlabel('x', fontsize=20, labelpad=100)
plt.ylabel('y', fontsize=20, labelpad=100)
plt.title('graph')
plt.plot(x, Px * Tx, 'black', label='T(x) = sin(x)\nP(x) = x^2 - 15x + 20\ny = T(x)P(X)')
plt.legend(loc='upper left')
plt.show()
'''
'''
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y, 'red', label='y=sin(x)', marker='^', mfc='red')
plt.plot(x, z, 'blue', label='y=cos(x)', linestyle='--', marker='o', mfc='blue')
plt.legend(loc='upper left')
plt.show()
'''
''' Сохранение фигуры
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, y, 'red', label='y=sin(x)', marker='^', mfc='red')
plt.plot(x, z, 'blue', label='y=cos(x)', linestyle='--', marker='o', mfc='blue')
plt.legend(loc='upper left')
plt.savefig('graph')
plt.show()
'''
# OpenCV
'''
image = cv2.imread('graph.png')
cv2.imshow('image', image)
cv2.waitKey(0)
'''
'''
image = cv2.imread('graph.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', image)
cv2.waitKey(0)
'''
'''
image = cv2.imread('graph.png', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (300, 300))
cv2.imshow('image', image)
cv2.waitKey(0)
'''
'''
pic_name = 'graph.png'
image = cv2.imread(pic_name, cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (300, 300))
part1 = image[:, :image.shape[1] // 2]
part2 = image[:, image.shape[1] // 2:]
pic1 = pic_name.replace('.', '1.')
pic2 = pic_name.replace('.', '2.')
cv2.imwrite(pic1, part1)
cv2.imwrite(pic2, part2)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.imshow('1', part1)
cv2.waitKey(0)
cv2.imshow('2', part2)
cv2.waitKey(0)
'''
pic_name = 'graph.png'
pic1 = pic_name.replace('.', '1.')
pic2 = pic_name.replace('.', '2.')
part1 = cv2.imread(pic1)
part2 = cv2.imread(pic2)
res = np.concatenate((part1, part2), axis=1)
cv2.imshow('res', res)
cv2.waitKey(0)
