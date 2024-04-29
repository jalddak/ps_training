def solution(a, b, n):
    answer = 0
    while n >= a:
        change = n//a * b
        answer += change
        n = n%a + change
    return answer