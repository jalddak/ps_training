a = "qwerasd"
a = list(a)
a[0], a[-1] = a[-1], a[0]
stack = []
for _ in range(10):
    stack.append(''.join(a))
print(stack)
print(list(set(stack)))