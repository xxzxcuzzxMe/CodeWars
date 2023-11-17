def longest_consec(strarr, k):
    n=len(strarr)
    
    if n==0 or k>n or k<=0:
        return ""
    longer=""
    for i in range(n - k + 1):
        x=''.join(strarr[i:i+k])
        if len(x)>len(longer):
            longer=x
        return longer