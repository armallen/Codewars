from scipy.signal import convolve2d

KERNEL = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]


def conway(x, y):
    # less than two neighbours
    if x < 2:
        return 0
    # Two or three neighbours
    if (x == 2 and y == 1) or (x == 3):
        return 1
    if x > 3:
        return 0

    return 0


# Computes next generation of a "game of life" table input
def next_gen(cells):
    if len(cells) > 0:
        # Using convolution : avoid writing longer code, but less memory efficient
        cells_cv = convolve2d(cells, KERNEL, mode='same', boundary='fill', fillvalue=0)
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                cells[i][j] = conway(cells_cv[i][j], cells[i][j])
    return cells
