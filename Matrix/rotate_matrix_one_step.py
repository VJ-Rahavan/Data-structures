def rotate_matrix(mat):
    n = len(mat)
    m = len(mat[0])

    top = 0
    bottom = n - 1
    left = 0
    right = m - 1

    while top < bottom and left < right:

        prev = mat[top][left]

        # Move right
        for j in range(left + 1, right + 1):
            temp = mat[top][j]
            mat[top][j] = prev
            prev = temp

        # Move down
        for i in range(top + 1, bottom + 1):
            temp = mat[i][right]
            mat[i][right] = prev
            prev = temp

        # Move left
        for j in range(right - 1, left - 1, -1):
            temp = mat[bottom][j]
            mat[bottom][j] = prev
            prev = temp

        # Move up
        for i in range(bottom - 1, top - 1, -1):
            temp = mat[i][left]
            mat[i][left] = prev
            prev = temp

        top += 1
        bottom -= 1
        left += 1
        right -= 1

    return mat