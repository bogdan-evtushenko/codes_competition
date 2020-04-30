def algorithm(matrix, height, width, player, winCount):
    i = 0
    while(matrix[i][winCount - 1] != '-1'):
        i += 1
    matrix[i][winCount - 1] = player
    return matrix