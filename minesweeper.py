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


def reveal_fields(mines, board, points, x, y):
    # check if the revealed square contains a mine
    if (x, y) in points:
        return
    points.add((x, y))
    if (x, y) in mines:
        return 1
    # check if all non-mine squares have been revealed
    if len(points) == (len(board) * len(board[0]) - len(mines)):
        return 2
    if board[x][y] == '0':
        # Reveal adjacent fields.
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Checking if an adjacent square is on the board
                if 0 <= x + i < len(board) and 0 <= y + j < len(board[0]):
                    reveal_fields(mines, board, points, x + i, y + j)
    else:
        # Pole ma wartość różną od zera.
        return


def print_board(board, points):
    rows = len(board)
    columns = len(board[0])
    # print column numbers
    print("   " + chr(9553), end="")
    for i in range(columns):
        if i > 9:
            print(f"{str(i)} {chr(9553)}", end="")
        else:
            print(f" {str(i)} {chr(9553)}", end="")
    print()

    print(end="")
    for i in range(columns+1):
        print((chr(9552) * 3) + chr(9580), end="")
    print()
    # print row numbers and contents of each square
    for i in range(rows):
        if i > 9:
            print(f"{str(i)} {chr(9553)}", end="")
        else:
            print(f" {str(i)} {chr(9553)}", end="")
        for j in range(columns):
            if (i, j) in points:
                # if a square has been revealed, print its contents in yellow
                if board[i][j] != '*':
                    print(f"{Fore.YELLOW} {board[i][j]} {Style.RESET_ALL}{chr(9553)}", end="")
                else:
                    print(f"{Fore.RED} * {Style.RESET_ALL}{chr(9553)}", end="")
            else:
                print(f"{Fore.BLUE} X {Style.RESET_ALL}{chr(9553)}", end="")
        print("\n", end="")
        for z in range(columns+1):
            print((chr(9552) * 3) + chr(9580), end="")
        print()
