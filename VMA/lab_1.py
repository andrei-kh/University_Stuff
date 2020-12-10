import numpy as np
import time

start_time = int(round(time.time() * 1000))

matrix = np.random.uniform(-100, 100, (3, 3))

normal = np.sum(np.absolute(matrix), axis=1).max()

end_time = int(round(time.time() * 1000))
print(matrix)
print('Normal: ', normal)
print('Time: ', end_time - start_time, 'ms')