def shipsPlacement():
    # (size (1-4), [coords (x, y)(0-9) )], route ('left', 'right', 'top', 'bottom') )
    return (
        [4, [0, 0], 'right'],
        [3, [2, 0], 'right'],
        [3, [9, 2], 'top'],
        [2, [0, 5], 'bottom'],
        [2, [0, 9], 'bottom'],
        [2, [7, 9], 'left'],
        [1, [0, 7], 'right'],
        [1, [5, 3], 'right'],
        [1, [5, 7], 'right'],
        [1, [3, 9], 'right']
    )

def algorithm(matrix):
    # matrix[x][y] == '-1' - empty
    # matrix[x][y] == '-' - miss
    # matrix[x][y] == '+' - hit
    for x in range(10):
        for y in range(10):
            if matrix[x][y] == '-1':
                return x, y