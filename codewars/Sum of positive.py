def positive_sum(arr):
    result = []
    for i in arr:
        if i > 0:
            result.append(i)
    return sum(result)
