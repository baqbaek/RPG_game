import numpy as np
import random as rand

matrix = np.zeros((10, 20), dtype=str)
matrix[:, :] = '-'
matrix[1:-1, :] = '|'
matrix[1:-1, 1:-1] = ' '

for i in range(0, 5):
    row = rand.randint(1, 8)
    col = rand.randint(1, 18)
    matrix[row][col] = 'E'

print(' ', end='  ')
for i in range(0, 20):
    if i == 19:
        print(chr(65 + i))
    else:
        print(chr(65 + i), end=' ')

x = 0
for i in matrix:
    print(x, end='  ')
    x += 1
    print(' '.join(i))
