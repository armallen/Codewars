def triangle(mat, i, j, a, b, n):
    if a == 2:
        mat[i][j] = 1
        mat[i + 1][j] = 1
        mat[i + 1][j + 1] = 1
    else:
        triangle(mat, i, j, a / 2, b / 2, n)
        triangle(mat, i + a / 2, j, a / 2, b / 2, n)
        triangle(mat, i + a / 2, j + b / 2, a / 2, b / 2, n)


def sierpinski(n):
    size = pow(2, n)
    if n == 0:
        return "L"
    # Starting mat
    mat = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        mat[i][0] = 1
        mat[i][i] = 1
        mat[size - 1][i] = 1

    triangle(mat, 0, 0, size, size, n)
    s = ""
    for ind, vec in enumerate(mat):
        for indval, val in enumerate(vec):
            if indval <= ind:
                if val == 1:
                    s += "L"
                    if indval != ind:
                        s += " "
                else:
                    s += '  '
                if (indval == ind) and (ind != (len(mat) - 1)):
                    s += "\n"
    return s
