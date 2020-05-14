def algorithm(matrix, height, width, player, winCount):
    i = 0
    while(i < height and matrix[i][winCount - 1] != '-1'):
        i += 1

    if (i == height):
        for i1 in range(height):
            for j1 in range(width):
                if (matrix[i1][j1] == '-1'):
                    matrix[i1][j1] = player
                    return matrix
    else:
        matrix[i][winCount - 1] = player

    return matrix