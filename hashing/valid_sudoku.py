"""
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# @param A : tuple of strings
# @return an integer
def isValidSudoku(self, A):
    row_sets = [set() for _ in range(9)]
    column_sets = [set() for _ in range(9)]
    box_sets = [set() for _ in range(9)]

    def add_row_set(i, val):
        if val in row_sets[i]:
            return False
        else:
            row_sets[i].add(val)
            return True

    def add_column_set(j, val):
        if val in column_sets[j]:
            return False
        else:
            column_sets[j].add(val)
            return True

    def add_box_set(i, j, val):
        idx = 3 * (i // 3) + (j // 3)
        if val in box_sets[idx]:
            return False
        else:
            box_sets[idx].add(val)
            return True

    for i in range(9):
        for j in range(9):
            val = A[i][j]
            if val != ".":
                success = add_row_set(i, val) and add_column_set(j, val) and add_box_set(i, j, val)
                if not success:
                    return 0

    return 1
