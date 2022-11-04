def recursion(stack):
    spelling = stack.pop()
    if spelling == 'A':
        stack.append('E')
    elif spelling == 'E':
        stack.append('I')
    elif spelling == 'I':
        stack.append('O')
    elif spelling == 'O':
        stack.append('U')
    else:
        stack = recursion(stack)

    return stack

def solution(word):
    answer = 0
    stack = []
    while True:
        if len(stack) < 5:
            stack.append('A')
            answer += 1
        else:
            stack = recursion(stack)
            answer += 1
        stack_str = ''.join(stack)
        if word == stack_str:
            return answer