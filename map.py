import numpy as np
import random as rand

import main
import soldier

matrix = np.zeros((10, 20), dtype=str)
matrix[:, :] = '-'
matrix[1:-1, :] = '|'
matrix[1:-1, 1:-1] = ' '


def enemy_spawn(lvl):
    for i in range(0, lvl):
        row = rand.randint(1, 8)
        col = rand.randint(1, 18)
        matrix[row][col] = 'E'


def player_spawn():
    row = rand.randint(1, 8)
    col = rand.randint(1, 18)
    matrix[row][col] = 'P'


def display_map():
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


def move_player(direction):
    row, col = np.where(matrix == 'P')
    row, col = int(row), int(col)
    if direction == 'up':
        if row > 1:
            matrix[row][col] = ' '
            matrix[row - 1][col] = 'P'
        else:
            print("Can't move in that direction")
    elif direction == 'down':
        if row < 8:
            matrix[row][col] = ' '
            matrix[row + 1][col] = 'P'
        else:
            print("Can't move in that direction")
    elif direction == 'left':
        if col > 1:
            matrix[row][col] = ' '
            matrix[row][col - 1] = 'P'
        else:
            print("Can't move in that direction")
    elif direction == 'right':
        if col < 18:
            matrix[row][col] = ' '
            matrix[row][col + 1] = 'P'
        else:
            print("Can't move in that direction")
    else:
        print("Invalid direction")
    while True:

        display_map()
        row, col = np.where(matrix == 'P')
        row, col = int(row), int(col)
        if matrix[row - 1][col] == 'E' or matrix[row + 1][col] == 'E' or \
                matrix[row][col - 1] == 'E' or matrix[row][col + 1] == 'E':
            print("Enemy found!")
            main.selected_soldier.actions()

        direction = input("Move in which direction? (up, down, left, right) ")
        move_player(direction)


'''
enemy_spawn(int(input('Number of enemies: ')))
player_spawn()
display_map()
move_player(input('Direction: '))
'''
