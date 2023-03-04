from colorama import Fore, Style  # Add a color library
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


def create_board(mines, rows, columns, mine='*'):
    board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if (i, j) in mines:
                row.append(mine)
            else:
                row.append(str(number_of_neighbouring_mines(mines, i, j, rows, columns)))
        board.append(row)
    return board


def number_of_neighbouring_mines(n_mines, x, y, rows, columns):
    neighboring_mines = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x + i, y + j) in n_mines:
                neighboring_mines += 1
    return neighboring_mines


def reveal_fields(mines, board, points):
    x = get_number(0, len(board) - 1, "Podaj x")
    y = get_number(0, len(board[0]) - 1, "Podaj y")
    points.add((y, x))
    print_board(board, points)

    # check if the revealed square contains a mine
    if (y, x) in mines:
        return 1
    # check if all non-mine squares have been revealed
    if len(points) == (len(board) * len(board[0]) - len(mines)):
        return
    # recursively reveal adjacent squares
    return reveal_fields(mines, board, points)


def print_board(board, points):
    rows = len(board)
    columns = len(board[0])
    # print column numbers
    print("  ", end="")
    for i in range(columns):
        print(i, end=" ")
    print()

    # print row numbers and contents of each square
    for i in range(rows):
        print(i, end=" ")
        for j in range(columns):
            if (i, j) in points:
                # if a square has been revealed, print its contents in yellow
                print(Fore.YELLOW + board[i][j] + Style.RESET_ALL, end=" ")
            else:
                print(Fore.BLUE + 'X' + Style.RESET_ALL, end=" ")
        print()
