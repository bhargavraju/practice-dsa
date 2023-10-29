"""
Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.
"""


# @param A : list of list of chars
def solveSudoku(A):
    def is_safe(val, i, j, arr):
        for row in range(9):
            if arr[row][j] == str(val):
                return False
        for col in range(9):
            if arr[i][col] == str(val):
                return False
        top, left = i - i % 3, j - j % 3
        for row in range(top, top + 3):
            for col in range(left, left + 3):
                if arr[row][col] == str(val):
                    return False
        return True

    def first_blank(arr):
        for i in range(9):
            for j in range(9):
                if arr[i][j] == ".":
                    return i, j
        return -1, -1

    def rec_helper(arr):
        i, j = first_blank(arr)
        if i == j == -1:
            return True
        for val in range(1, 10):
            if is_safe(val, i, j, arr):
                arr[i][j] = str(val)
                if rec_helper(arr):
                    return True
                else:
                    arr[i][j] = "."
        return False

    rec_helper(A)
