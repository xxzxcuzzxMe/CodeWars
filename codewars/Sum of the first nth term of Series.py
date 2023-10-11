def series_sum(n):
    result = 0.0
    for x in range(n):
        result+= 1 / (1 + x * 3)
    return '%.2f' % result