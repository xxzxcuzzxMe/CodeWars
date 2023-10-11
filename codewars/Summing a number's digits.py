def sum_digits(number):
    number = str(number)
    result = []
    
    if number[0] == '-':
        number = number[1:]
    
    for i in number:
        result.append(i)
    
    return sum([int(digit) for digit in result])
