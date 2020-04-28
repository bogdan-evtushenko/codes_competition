from random import *

def getAnotherPlayer(player):
    if (player == 'o'):
        return 'x'
    else:
        return 'o'

def isSecondPlayerPlayPredictable(matrix, height, width, player):
    secondPlayer = getAnotherPlayer(player)
    evilCells = []
    wasEmptyCell = False

    for i in range(height):
        for j in range(width):
            if matrix[i][j] == secondPlayer:
                if (wasEmptyCell):
                    return 0
                evilCells.append((i, j))
            elif matrix[i][j] == '-1':
                wasEmptyCell = True

    for i in range(1, len(evilCells)):
        print(i)
        if (evilCells[i][0] == evilCells[i - 1][0] and evilCells[i][1] < evilCells[i - 1][1]):
            return 0
        elif (evilCells[i][0] < evilCells[i - 1][0]):
            return 0
    return 1

def algorithm(matrix, height, width, player):
    if (isSecondPlayerPlayPredictable(matrix, height, width, player)):
        return antiStupidAlgotithm(matrix, height, width, player)
    else:
        return randomAlgorithm(matrix, height, width, player)

def antiStupidAlgotithm(matrix, height, width, player):
    secondPlayer = getAnotherPlayer(player)

    countForWin = 3
    countEvil = 0
    isAlreadyPlaced = False
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == secondPlayer:
                countEvil += 1
            elif matrix[i][j] == '-1' and countEvil == countForWin - 1:
                matrix[i][j] = player
                isAlreadyPlaced = True
                break
        if isAlreadyPlaced: 
            break
        countEvil = 0
   
    for i in range(width, 0, -1):
        if (matrix[height - 1][i - 1] == '-1'):
            if (isAlreadyPlaced == False):
                matrix[height - 1][i - 1] = player
            break

    return matrix

def randomAlgorithm(matrix, height, width, player):
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