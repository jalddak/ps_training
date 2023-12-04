inorder = input()

postorder = ""

operand = set(['+', '-', '*', '/', '(', ')'])
stack = ['(']

def recursion(postorder):
    sp = stack.pop()
    while sp != '(':
        if sp == ')':
            recursion()
        postorder += sp
        sp = stack.pop()
    return postorder

for c in inorder:
    if c not in operand:
        postorder += c
        continue
    if stack[-1] in ['+', '-'] and c in ['*', '/', '(']:
        stack.append(c)
        continue
    if stack[-1] in ['+', '-', '*', '/'] and c == '(':
        stack.append(c)
        continue
    if c == ')':
        postorder = recursion(postorder)
        continue
    if c in ['+', '-']:
        while stack[-1] in ['*', '/', '+', '-']:
            postorder += stack.pop()
    elif c in ['*', '/']:
        while stack[-1] in ['*', '/']:
            postorder += stack.pop()
    stack.append(c)

postorder = recursion(postorder)
    
print(postorder)