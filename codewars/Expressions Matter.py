def expression_matter(a, b, c):
    result = []
    result.append (a * (b + c))
    result.append (a * b * c)
    result.append (a + b * c)
    result.append((a + b) * c)
    result.append(a + b + c)
    return max(result)