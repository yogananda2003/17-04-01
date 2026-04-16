def multiply_matrices(matrix_a, matrix_b):
    """Multiply two matrices and return the result matrix."""
    if not matrix_a or not matrix_b:
        raise ValueError("Both matrices must be non-empty.")

    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)

    if cols_a != rows_b:
        raise ValueError(
            "Matrix multiplication not possible: "
            "number of columns in A must equal number of rows in B."
        )

    # Validate rectangular shapes.
    if any(len(row) != cols_a for row in matrix_a):
        raise ValueError("Matrix A has inconsistent row sizes.")
    cols_b = len(matrix_b[0])
    if any(len(row) != cols_b for row in matrix_b):
        raise ValueError("Matrix B has inconsistent row sizes.")

    result = []
    for i in range(len(matrix_a)):
        result_row = []
        for j in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum += matrix_a[i][k] * matrix_b[k][j]
            result_row.append(cell_sum)
        result.append(result_row)
    return result


def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(" ".join(f"{value:6}" for value in row))
    print()


def main():
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    matrix_b = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]

    result = multiply_matrices(matrix_a, matrix_b)

    print_matrix(matrix_a, "Matrix A:")
    print_matrix(matrix_b, "Matrix B:")
    print_matrix(result, "A x B:")


if __name__ == "__main__":
    main()
