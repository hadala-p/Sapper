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
    # for i in range(n_rows):
    #     print(board[i])
    points = set()
    if reveal_fields(mines, board, points) == 1:
        print("Koniec gry, trafiono na bombe")
        return
    print("Wygrana, pozostaly tylko bomby!")


sapper()
