def solution(s):
    result = [ ]
    for i in s:
        if i.isupper():
            result.append(f' {i}')
        else:
            result.append(i)
    return ''.join(result)
    
            
            