def shipsPlacement():
    # (size (1-4), [coords (x, y)(0-9) )], route ('left', 'right', 'top', 'bottom') )
    return (
        [4, [4, 3], 'right'],
        [3, [0, 3], 'right'],
        [3, [6, 7], 'right'],
        [2, [7, 2], 'bottom'],
        [2, [0, 9], 'bottom'],
        [2, [2, 0], 'right'],
        [1, [2, 7], 'right'],
        [1, [7, 5], 'right'],
        [1, [9, 5], 'right'],
        [1, [8, 8], 'right']
    )

def algorithm(matrix):
    # matrix[x][y] == '-1' - empty
    # matrix[x][y] == '-' - miss
    # matrix[x][y] == '+' - hit
    for x in range(10):
        for y in range(10):
            if matrix[x][y] == '-1':
                return x, y