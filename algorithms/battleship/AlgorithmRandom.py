from random import randint

def shipsPlacement():
    # (size (1-4), [coords (x, y)(0-9) )], route ('left', 'right', 'top', 'bottom') )
    empty_cells = []
    for i in range(10):
        for j in range(10):
            empty_cells.append((i, j))
    occupied_cells = []
    routes = ['right', 'left', 'top', 'bottom']

    xy_rand = lambda : empty_cells[randint(0, len(empty_cells) - 1)]
    route_rand = lambda : routes[randint(0, len(routes) - 1)]

    def ship(size):
        while 1:
            x_start, y_start = xy_rand()
            route = route_rand()
            x_end, y_end = x_start, y_start
            x_end -= (size - 1) if route == 'top' else 0
            x_end += (size - 1) if route == 'bottom' else 0
            y_end += (size - 1) if route == 'right' else 0
            y_end -= (size - 1) if route == 'left' else 0
            if x_end < 0 or x_end > 9 or y_end < 0 or y_end > 9:
                continue

            cells = []
            for i in range(min(x_start, x_end), max(x_start, x_end) + 1):
                for j in range(min(y_start, y_end), max(y_start, y_end) + 1):
                    cells.append((i, j))

            if len(set(cells).intersection(occupied_cells)) != 0:
                continue

            cells = []
            for i in range(min(x_start, x_end) - 1, max(x_start, x_end) + 2):
                for j in range(min(y_start, y_end) - 1, max(y_start, y_end) + 2):
                    if 0 <= i <= 9 and 0 <= j <= 9:
                        cells.append((i, j))

            [occupied_cells.append(i) for i in cells]
            break

        return [size, [x_start, y_start], route]

    return (
         ship(4),
         ship(3),
         ship(3),
         ship(2),
         ship(2),
         ship(2),
         ship(1),
         ship(1),
         ship(1),
         ship(1)
    )

def algorithm(matrix):
    # matrix[x][y] == '-1' - empty
    # matrix[x][y] == '-' - miss
    # matrix[x][y] == '+' - hit
    empty_attack_cells = []

    for x in range(10):
        for y in range(10):
            if matrix[x][y] == '-1':
                empty_attack_cells.append((x, y))

    return empty_attack_cells[randint(0, len(empty_attack_cells) - 1)]