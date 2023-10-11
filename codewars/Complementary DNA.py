def DNA_strand(dna):
    result = ''
    for i in dna:
        if i == 'A':
            result +='T'
        elif i == 'T':
            result +='A'
        elif i == 'C':
            result += 'G'
        else :
            result +='C'
    return result