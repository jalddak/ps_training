def check(p):
    stack = []
    correct = True
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(0)
        elif len(stack) > 0:
            stack.pop()
        else:
            correct = False
            
    return correct

def slice_p(p):
    left = 0
    right = 0
    index = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right and left != 0:
            index = i + 1
            break
    u = p[:index]
    v = p[index:]
    return u, v

def solution(p):
    answer = ''
    correct = check(p)
    if not correct and p != '':
        u, v = slice_p(p)
        if check(u):
            answer = u + solution(v)
        else:
            answer += '('
            answer += solution(v)
            answer += ')'
            for letter in u[1:-1]:
                if letter == '(':
                    answer += ')'
                else:
                    answer += '('
    else:
        answer += p
        
    return answer