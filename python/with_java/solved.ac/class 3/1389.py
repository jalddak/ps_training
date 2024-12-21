# 플로이드 워셜

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# board = [[1e9 for _ in range(n+1)] for _ in range(n+1)]

# for _ in range(m):
#     n1, n2 = map(int, input().split())
#     board[n1][n2] = 1
#     board[n2][n1] = 1

# for i in range(1, n+1):
#     board[i][i] = 0
#     board[i][0] = 0

# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             board[a][b] = min(board[a][b], board[a][k] + board[k][b])

# cnt = 10000
# answer = 0
# for i in range(1, n+1):
#     temp = sum(board[i])
#     if cnt > temp:
#         cnt = temp
#         answer = i

# print(answer)

#bfs

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

relations = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    relations[n1].append(n2)
    relations[n2].append(n1)

answer = 0
cnt = 10000

for i in range(1, n+1):
    kbNum = [1e9 for _ in range(n+1)]
    kbNum[0] = 0
    kbNum[i] = 0
    q = deque([(i, 1)])
    while q:
        node, num = q.popleft()

        for f in relations[node]:
            if kbNum[f] > num:
                kbNum[f] = num
                q.append((f, num+1))
    
    temp = sum(kbNum)
    if cnt > temp:
        cnt = temp
        answer = i

print(answer)