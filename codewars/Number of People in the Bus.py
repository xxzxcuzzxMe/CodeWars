def number(bus_stops):
    temp = 0 
    for i in bus_stops:
        temp += i[0]
        temp -= i[1]
    return temp
