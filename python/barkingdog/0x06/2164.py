n = int(input())

cards = [i for i in range(1, n+1)]

from collections import deque
q = deque(cards)

while len(q) > 1:
    q.popleft()
    # q.append(q.popleft())
    q.rotate(-1)

print(q[0])