def solution(my_string, n):
    answer = ''
    for letter in my_string:
        for _ in range(n):
            answer += letter
    return answer