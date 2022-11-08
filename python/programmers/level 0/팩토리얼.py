def solution(n):
    answer = 1
    factorial = 1
    while True:
        if n < factorial:
            break
        else:
            answer += 1
            factorial *= answer
    answer -= 1
    return answer