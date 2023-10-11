def sum_array(arr):
    if arr is None:
        return 0

    if len(arr) <= 2:
        return 0
    else:
        sorted_arr = sorted(arr)
        sum_elements = sum(sorted_arr[1:len(sorted_arr)-1])
        return sum_elements