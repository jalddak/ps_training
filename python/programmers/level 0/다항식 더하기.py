def solution(polynomial):
    answer = ''
    x = 0
    상수 = 0
    p = polynomial.split()
    for num in p:
        if num[-1] == 'x':
            if len(num) == 1:
                x += 1
            else:
                x += int(num[:-1])
        elif num.isdigit():
            상수 += int(num)
            
    if x > 0 and 상수 > 0:
        if x == 1:
            answer = 'x + ' + str(상수)
        else:
            answer = str(x) + 'x + ' + str(상수)
    elif x > 0 and 상수 <= 0:
        if x == 1:
            answer = 'x'
        else:
            answer = str(x) + 'x'
    elif x <= 0 and 상수 > 0:
        answer = str(상수)
        
    return answer