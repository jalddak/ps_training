str1 = input()
boom = input()
length = len(boom)

stack = []

for a in str1:
    stack.append(a)
    if len(stack) < length or a != boom[-1]:
        continue
    if "".join(stack[len(stack)-length:]) == boom:
        for _ in range(length):
            stack.pop()

answer = "".join(stack)
if not answer:
    answer = "FRULA"
print(answer)