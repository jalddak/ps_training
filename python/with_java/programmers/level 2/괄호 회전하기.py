from collections import deque

def check(s):
    stack = []
    result = True
    for i in range(len(s)):
        c = s[i]
        if c in ['[', '{', '(']:
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = False
                break
        elif c == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                result = False
                break
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = False
                break
    if stack:
        result = False
    return result

def solution(s):
    s = deque(s)
    answer = 0
    for _ in range(len(s)):
        if check(s): answer += 1
        s.append(s.popleft())
    return answer