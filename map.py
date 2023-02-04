import numpy as np

matrix = np.zeros((10, 20), dtype=str)
matrix[:, :] = '--'
matrix[1:-1, :] = '|'
matrix[1:-1, 1:-1] = 'x'

for row in matrix:
    print(''.join(row))

