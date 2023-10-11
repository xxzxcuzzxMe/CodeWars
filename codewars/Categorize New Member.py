def open_or_senior(members):
    result = []
    for member in members:
        age, handicap = member
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

