# BFS

from collections import deque

board = [[0 for _ in range(10)] for _ in range(10)]
N, M = list(map(int, input().split()))

for _ in range(N):
    d, a = list(map(lambda x: x-1, list(map(int, input().split()))))
    board[d//10][d%10] = a

for _ in range(M):
    d, a = list(map(lambda x: x-1, list(map(int, input().split()))))
    board[d//10][d%10] = a
            
visited = [[False for _ in range(10)] for _ in range(10)]

queue = deque([[0, 0]])
visited[0][0] = True

while len(queue) != 0:
    loca, cnt = queue.popleft()
    cnt += 1
    for i in range(1, 7):
        n_loca = loca + i
        if 0 <= n_loca <= 99:
            if not visited[n_loca//10][n_loca%10]:
                visited[n_loca//10][n_loca%10] = True
                if board[n_loca//10][n_loca%10] != 0:
                    n_loca = board[n_loca//10][n_loca%10]
                    if not visited[n_loca//10][n_loca%10]:
                        visited[n_loca//10][n_loca%10] = True
                        queue.append([n_loca, cnt])
                else:
                    queue.append([n_loca, cnt])
        if n_loca == 99:
            print(cnt)
            quit()
    