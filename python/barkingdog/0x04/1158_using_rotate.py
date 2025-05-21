from collections import deque

n, k = map(int, input().split())

q = deque([i for i in range(1, n+1)])

result = []
while q:
    q.rotate(-(k-1))
    result.append(q.popleft())

print("<" + ", ".join(map(str, result)) + ">")