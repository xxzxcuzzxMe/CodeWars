def multiplication_table(size):
    result = []
    for i in range(1, size + 1):
        matrix_el = []
        for j in range(1, size + 1):
            matrix_el.append(i * j)
        result.append(matrix_el)
    return result
    