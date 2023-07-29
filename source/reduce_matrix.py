# Completar los comentarios de la siguiente funcion

def reduce_matrix(m):
    """
    Funcion que implementa el algoritmo de Gauss-Jordan para la reduccion de una matriz
    """
    matrix = m.astype(float).copy()
    pivot_col = 0
    n_rows, n_cols = matrix.shape

    for row in range(n_rows):

        if pivot_col >= n_cols:
            return matrix.round(2)

        # ....
        row_pivot = row

        # ....
        while abs(matrix[row_pivot][pivot_col]) < 1e-5:
            row_pivot += 1

            # ....
            if row_pivot == n_rows:
                # ....
                row_pivot = row
                pivot_col += 1
                if n_cols == pivot_col:
                    return matrix.round(2)
            else:
                # ....
                matrix[[row_pivot,row]] = matrix[[row, row_pivot]]

        # .....
        pivot = matrix[row][pivot_col]
        matrix[row] = [mrx / float(pivot) for mrx in matrix[row]]

        # ....
        for other_row in range(n_rows):
            if other_row != row:
                # ....
                below_pivot = matrix[other_row][pivot_col]
                matrix[other_row] = [iv - below_pivot * rv for rv, iv in zip(matrix[row], matrix[other_row])]
        pivot_col += 1
    return matrix.round(2)