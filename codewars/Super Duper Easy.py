def problem(a):
    if isinstance(a, int) or isinstance(a,float):
        result = a * 50 + 6
        return result
    else:
        return "Error"