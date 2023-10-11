def count_digits(num, d):
    count = 0
    for digit in str(num):
        if int(digit) == d:
            count += 1
    return count
