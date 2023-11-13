def flatten_and_sort(array):
    arr = []
    for i in array:
        for j in i:
            arr.append(j)
    return sorted(arr)