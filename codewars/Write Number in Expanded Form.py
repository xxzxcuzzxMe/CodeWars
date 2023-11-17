def expanded_form(num):
    num_str = str(num)
    result = []  
    for i in range(len(num_str)):
        curr_digit = num_str[i]
        if curr_digit != '0':  
            result.append(curr_digit + '0' * (len(num_str) - i - 1))
    return ' + '.join(result)


