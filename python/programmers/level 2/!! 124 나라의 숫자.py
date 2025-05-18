def solution(n):
    answer = ''
    n -= 1
    while True:
        나머지 = n % 3
        if 나머지 == 0:
            answer += '1'
        elif 나머지 == 1:
            answer += '2'
        else:
            answer += '4'
        if n < 3:
            break
        n //= 3
        n -= 1
    answer = list(answer)
    answer.reverse()
    answer = ''.join(answer)
    return answer