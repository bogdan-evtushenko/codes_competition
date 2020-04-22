from random import *

def algorithm(matrix, height, width, player):
    emptyCells = []
    
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == '-1':
                emptyCells.append((i, j))
    
    indexes = emptyCells[randint(0, len(emptyCells) - 1)]
    
    x = indexes[0]
    y = indexes[1]
    
    matrix[x][y] = player
    
    return matrix
