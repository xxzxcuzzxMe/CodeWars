def sort_array(arr):
    odd_arr = []
    for i in arr:
        if i % 2 != 0:
            odd_arr.append(i)
    odd_arr = sorted(odd_arr)
    for j in arr:
        if j % 2 == 0:
            odd_arr.insert(arr.index(j), j)
    return odd_arr