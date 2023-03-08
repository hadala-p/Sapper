from minesweeper import *
# define minimum and maximum number of rows and columns
min_rows = 8
max_rows = 30
min_columns = 8
max_columns = 24


def sapper():
    n_rows = get_number(min_rows, max_rows, "Podaj liczbę wierszy")
    n_columns = get_number(min_columns, max_columns, "Podaj liczbę kolumn")
    mine_ratio = int((n_rows * n_columns) * 0.17)
    mines = lay_mines(mine_ratio, n_rows, n_columns)
    board = create_board(mines, n_rows, n_columns)
    points = set()
    while True:
        print_board(board, points)
        x = get_number(0, len(board) - 1, "Podaj x: ")
        y = get_number(0, len(board[0]) - 1, "Podaj y: ")
        reveal_fields(mines, board, points, x, y)
        if (x, y) in mines:
            print_board(board, points)
            print("Koniec gry, trafiono na bombe")
            return
        if len(points) == (len(board) * len(board[0]) - len(mines)):
            print_board(board, points)
            print("Wygrana, pozostaly tylko bomby!")
            return


sapper()
