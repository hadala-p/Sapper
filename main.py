from minesweeper import *
from colorama import Fore, Back, Style

min_rows = 8
max_rows = 30
min_columns = 8
max_columns = 24


def sapper():
    n_rows = 3
    n_columns = 3
    # n_rows = get_number(min_rows, max_rows, "Podaj liczbę wierszy")
    # n_columns = get_number(min_columns, max_columns, "Podaj liczbę kolumn")
    mines = lay_mines(int((n_rows * n_columns) * 0.17), n_rows, n_columns)
    n_board = create_board(mines, n_rows, n_columns)
    for i in range(n_rows):
        print(n_board[i])
    if reveal_fields(mines, n_board, n_rows, n_columns, set()) == 1:
        print("Koniec gry, trafiono na bombe")
        return
    print("Wygrana, pozostaly tylko bomby!")


sapper()
