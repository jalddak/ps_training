def solution(n):
    answer = 0
    이진수 = bin(n)[2:]
    one_cnt = 이진수.count('1')
    while True:
        n += 1
        if bin(n)[2:].count('1') == one_cnt:
            answer = n
            break
    return answer