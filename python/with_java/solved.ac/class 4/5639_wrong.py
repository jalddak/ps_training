import sys
input = sys.stdin.readline

stack = []
result = []
while True:
    try:
        while True:
            n = int(input())
            if not stack or stack[-1] > n:
                stack.append(n)
            else:
                result.append(stack.pop())
                while len(stack) > 1 and stack[-2] < n:
                    result.append(stack.pop())
                stack.append(n)
            print(stack)
            print(result)

    except:
        break

result += reversed(stack)
for r in result:
    print(r)