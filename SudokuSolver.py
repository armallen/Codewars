REF = {1, 2, 3, 4, 5, 6, 7, 8, 9}
SIZE = 9
SIZE_SQUARE = 3


# Utility function : flattens list
def flatten(seq, container=None):
    if container is None:
        container = []
    for s in seq:
        if hasattr(s, '__iter__'):
            flatten(s, container)
        else:
            container.append(s)
    return container


# Sudoku solver
class Sudoku(object):
    def __init__(self, sud):
        self.sudoku = sud
        self.tsudoku = [list(x) for x in zip(*self.sudoku)]

    # Sudoku is valid if it is full
    def is_valid(self):
        return flatten(self.sudoku).count(0) == 0

    # Sets value in the list
    def set_val(self, i, j, val):
        self.sudoku[i][j] = val
        self.tsudoku[j][i] = val

    # Get value from the lis
    def get_val(self, i, j):
        return self.sudoku[i][j]

    # Get the 3x3 square associated to the point of coordinates i,j
    def get_square(self, i, j):
        lc = int(i / 3)
        cc = int(j / 3)
        return [self.sudoku[SIZE_SQUARE * lc + k][SIZE_SQUARE * cc + l] for k in range(SIZE_SQUARE) for l in
                range(SIZE_SQUARE)]

    # Get the i-th row
    def get_row(self, i):
        return [self.sudoku[i][x] for x in range(SIZE)]

    # Get the j-th col
    def get_col(self, j):
        return [self.sudoku[x][j] for x in range(SIZE)]

    # Use the 3 basic rules to simplify current board
    def simplify(self):
        if not self.is_valid():
            changed = True
            while changed:
                changed = False
                for ll in range(0, SIZE):
                    for lc in range(0, SIZE):
                        if self.get_val(ll, lc) == 0:
                            values = set(REF) - set(self.get_row(ll)) - set(self.get_col(lc)) - set(
                                self.get_square(ll, lc))
                            if 1 == len(values):
                                self.set_val(ll, lc, next(iter(values)))
                                changed = True


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    sol = Sudoku(puzzle)
    sol.simplify()
    print(sol.sudoku)

if __name__ == "__main__":
    puzzleTest = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    sudoku(puzzleTest)
