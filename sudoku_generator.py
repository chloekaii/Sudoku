import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(0, 9)] for j in range(0, row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    def print_board(self):
        print(self.board)

    def valid_in_row(self, row, num):
        for i in range(0, 9):
            if num == self.board[row][i]:
                return False
        return True

    def valid_in_col(self, col, num):
        for i in range(0, 9):
            if num == self.board[i][col]:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):  # checks each column in the box
        for i in range(0, 3):
            for j in range(0, 3):
                box_checked = self.board[row_start + j][col_start + i]
                if num == box_checked:
                    return False
            return True

    def is_valid(self, row, col, num):
        col_isvalid = self.valid_in_col(col, num)
        row_isvalid = self.valid_in_row(row, num)
        box_isvalid = self.valid_in_box(self.__get_box_values(row, col)[0], self.__get_box_values(row, col)[1], num)
        if col_isvalid and row_isvalid and box_isvalid:
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        for i in range(0, 3):
            for j in range(0, 3):
                rand_num = random.randint(1, 9)
                generating_num = True
                while generating_num:
                    if self.valid_in_box(row_start, col_start, rand_num):
                        self.board[row_start + i][col_start + j] = rand_num
                        generating_num = False
                    else:
                        rand_num = random.randint(1, 9)

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        for i in range(0, self.removed_cells):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            removing_cell = True
            while removing_cell:
                if self.board[row][col] == 0:
                    row = random.randint(0, 8)
                    col = random.randint(0, 8)
                else:
                    self.board[row][col] = 0
                    removing_cell = False

    def __get_box_values(self, row, col):
        if 0 <= row <= 2:
            self.row_start = 0
        elif 3 <= row <= 5:
            self.row_start = 3
        else:
            self.row_start = 6
        if 0 <= col <= 2:
            self.col_start = 0
        elif 3 <= col <= 5:
            self.col_start = 3
        else:
            self.col_start = 6
        return [self.row_start, self.col_start]


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
