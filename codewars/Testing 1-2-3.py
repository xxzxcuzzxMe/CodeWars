def number(lines):
    count = 1
    result = []
    for x in lines:
        result.append(str(count) + ': ' + x)
        count += 1
    return result