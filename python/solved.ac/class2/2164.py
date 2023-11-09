from collections import deque

N = int(input())

l = deque([i for i in range(1, N+1)])


check = True
while len(l) != 1:
    if check:
        l.popleft()
    else:
        l.append(l.popleft())
    check = not check

print(l[0])