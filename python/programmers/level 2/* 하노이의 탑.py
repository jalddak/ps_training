def hanoi(n, s, e, t):
    if n == 1:
        return [[s, e]]
    return hanoi(n-1, s, t, e) + [[s, e]] + hanoi(n-1, t, e, s)

def solution(n):
    answer = hanoi(n, 1, 3, 2)
    return answer