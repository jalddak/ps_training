from collections import deque

n = int(input())
board = []
# baby shark size
bss = 2
# 거리가 같으면 위쪽, 왼쪽 먼저 먹기
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

queue = deque([])
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(n):
        if board[i][j] == 9:
            queue.append([i, j, 0, -1])
            visited[i][j] = 1
            board[i][j] = 0

# 물고기 먹은 수
cnt = 0
last = 0
# 먹을 수 있는 가장 가까운 물고기가 거리가 같다면 위쪽, 왼쪽먼저
while len(queue) != 0:
    bsl = queue.popleft()
    if 0 < board[bsl[0]][bsl[1]] < bss:
        cnt += 1
        if cnt == bss:
            bss += 1
            cnt = 0
        board[bsl[0]][bsl[1]] = 0
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[bsl[0]][bsl[1]] = 1
        last = bsl[2]
        queue = deque([])

    time = bsl[2] + 1
    for i in range(4):
        ny = bsl[0] + dy[i]
        nx = bsl[1] + dx[i]
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] <= bss and visited[ny][nx] != 1:
            visited[ny][nx] = 1
            queue.append([ny, nx, time])
            queue = list(queue)
            queue.sort(key = lambda x:(x[2], x[0], x[1]))
            queue = deque(queue)
print(last)
