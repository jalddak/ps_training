original = input()
boom = input()
stack = []
check_len = len(boom)

for a in original:
    stack.append(a)
    if a == boom[-1] and len(stack) >= check_len and ''.join(stack[-check_len:]) == boom:
        for _ in range(check_len):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))