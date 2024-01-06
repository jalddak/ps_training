k = int(input())
command = list(input().split())

stack = []
min_n = ""
max_n = ""

def recursion(depth):
    global k, command, stack, min_n, max_n
    if depth == k:
        max_n = "".join(map(str, stack))
        if min_n == "":
            min_n = max_n
        return
    
    for n in range(10):
        if n not in stack:
            if command[depth] == '<' and stack[-1] > n:
                continue
            if command[depth] == '>' and stack[-1] < n:
                continue
            stack.append(n)
            recursion(depth+1)
            stack.pop()


for n in range(10):
    stack.append(n)
    recursion(0)
    stack.pop()

print(max_n)
print(min_n)