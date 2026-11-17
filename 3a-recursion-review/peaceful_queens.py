n = 4
row = {}
col = {}
diagonal = {}

def generate_n_chess_grid(n):
    return [['.'] * 4 for _ in range(4)]

def add(coordinate, grid):
    diagonal[coordinate] = True
    x = coordinate[0]
    y = coordinate[1]
    row[x] = True
    col[y] = True
    grid[x][y] = 'Q'

def remove(coordinate, grid):
    diagonal[coordinate] = False
    x = coordinate[0]
    y = coordinate[1]
    row[x] = False
    col[y] = False
    grid[x][y] = '.'

def safe(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    diag_sum = x + y
    diag_diff = x - y
    found = False
    for d in diagonal:
        if d != coordinate and (d[0] + d[1] == diag_sum or d[0] - d[1] == diag_diff) and diagonal[d]: # noqa: E501
            found = True
    c1 = not (x in row and row[x])
    c2 = not (y in col and col[y])
    c3 = not found
    # print(coordinate, c1, c2, c3, row, col, diagonal, end='\n\n')
    return c1 and c2 and c3

def peaceful_queens(n, index, valid, result):
    if index == n:
        result.append([row[:] for row in valid])
        return
    for i in range(n):
        coordinate = (index, i)
        if safe(coordinate):
            add(coordinate, valid)
            peaceful_queens(n, index + 1, valid, result)
            remove(coordinate, valid)
    return result

def pretty_print(answers):
    if answers:
        for answer in answers:
            for row in answer:
                print(row)
            print('*' * 20)

answers = peaceful_queens(n, 0, generate_n_chess_grid(n), [])
pretty_print(answers)
