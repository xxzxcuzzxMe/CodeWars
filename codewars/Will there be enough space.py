def enough(cap, on, wait):
    result = cap - on 
    if wait > result :
        return wait - result
    else:
        return 0