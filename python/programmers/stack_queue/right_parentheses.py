def solution(s):
    stack = []
    for word in s:
        if word == '(':
            stack.append(0)
        elif word == ')' and len(stack) != 0:
            stack.pop();
        else:
            return False
            
    if len(stack) == 0:
        answer = True
    else:
        answer = False

    return answer