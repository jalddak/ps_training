def solution(n, s):
    if s // n == 0:
        return [-1]
    answer = [s // n for _ in range(n)]
    per = s % n
    i = n-1
    for _ in range(per):
        answer[i] += 1
        i -= 1
    return answer