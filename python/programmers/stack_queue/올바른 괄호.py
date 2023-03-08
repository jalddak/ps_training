def solution(s):
    answer = True
    n = 0
    for w in s:
        if n == 0 and w == ')':
            return False
        elif w == '(':
            n += 1
        elif w == ')':
            n -= 1
    if n != 0:
        return False
    return answer