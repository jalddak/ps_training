def main(s):
    result = ''
    for a in s:
        asc = ord(a)
        if 48 <= asc <= 57:
            result += number(a)
        elif 97 <= asc <= 122:
            result += lower(asc)
        elif 65 <= asc <= 90:
            result += upper(asc)
    
    print(result)
    return result

def number(n):
    n = int(n)
    if n != 0:
        n = 10 - n
    return str(n)

def lower(asc):
    m = asc - 97
    asc += 25 - 2*m
    return chr(asc)


def upper(asc):
    asc += 1
    if asc == 91:
        asc = 65
    return chr(asc)



main('123abcABC')
main('i0Lg8HZ')