def multi_table(number):
    result = ''
    for i in range(1, 11):
        equation = f'{i} * {number} = {i * number}'
        result += equation + '\n'
    return result[:-1]
