import random


def get_number(a, b, text):
    while True:
        temp = int(input(text))
        if a <= temp <= b:
            return temp
        print(f"Podano zla liczbe, podaj jescze raz z zakresu od {a} do {b}")


def lay_mines(n_mines, rows, columns):
    mines = set()
    while len(mines) < n_mines:
        i = random.randrange(rows)
        j = random.randrange(columns)
        mines.add((i, j))
    return mines


def create_board(n_mines, rows, columns, mine='*'):
    board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if (i, j) in n_mines:
                row.append(mine)
            else:
                row.append(number_of_neighbouring_mines(n_mines, i, j, rows, columns))
        board.append(row)
    return board


def number_of_neighbouring_mines(n_mines, x, y, rows, columns):
    neighboring_mines = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if (x + i, y + j) in n_mines:
                    neighboring_mines += 1
    return str(neighboring_mines)


def reveal_fields(n_mines, board, rows, columns, points):
    x = get_number(0, rows-1, "Podaj x")
    y = get_number(0, columns-1, "Podaj y")
    points.add((y, x))
    print_board(board, rows, columns, points)
    if len(points) == (rows * columns - len(n_mines)):
        return
    if (y, x) in n_mines:
        return 1
    return reveal_fields(n_mines, board, rows, columns, points)


def print_board(board, rows, columns, points):
    new_board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if (i, j) in points:
                row.append(board[i][j])
            else:
                row.append('X')
        new_board.append(row)
    for i in range(rows):
        print(new_board[i])
