N, M = map(int, input().split())

board = [list(map(lambda x : x+9, list(map(int, input().split())))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

island_num = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 10 and not visited[i][j]:
            stack = [[i, j]]
            visited[i][j] = True
            while len(stack) != 0:
                y, x = stack.pop()
                board[y][x] = island_num
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 10 and not visited[ny][nx]:
                        stack.append([ny, nx])
                        visited[ny][nx] = True
            island_num += 1


distance_board = [[N * M for _ in range(island_num)] for _ in range(island_num)]

for i in range(N):
    start = -1
    cnt = 0
    for j in range(M):
        if board[i][j] == 9:
            if start == -1:
                continue
            cnt += 1
        if board[i][j] != 9:
            if start == -1:
                start = board[i][j]
                continue
            if start == board[i][j]:
                cnt = 0
                continue
            if cnt >= 2:
                distance_board[start][board[i][j]] = min(distance_board[start][board[i][j]], cnt)
                distance_board[board[i][j]][start] = distance_board[start][board[i][j]]
            start = board[i][j]
            cnt = 0

for j in range(M):
    start = -1
    cnt = 0
    for i in range(N):
        if board[i][j] == 9:
            if start == -1:
                continue
            cnt += 1
        if board[i][j] != 9:
            if start == -1:
                start = board[i][j]
                continue
            if start == board[i][j]:
                cnt = 0
                continue
            if cnt >= 2:
                distance_board[start][board[i][j]] = min(distance_board[start][board[i][j]], cnt)
                distance_board[board[i][j]][start] = distance_board[start][board[i][j]]
            start = board[i][j]
            cnt = 0


min_info = [0, 0, N * M]
for i in range(island_num):
    for j in range(i, island_num):
        if distance_board[i][j] < min_info[2]:
            min_info = [i, j, distance_board[i][j]]


visited = [False for _ in range(island_num)]

bridge_info = [min_info]
result = 0

while len(bridge_info) != 0:
    f, s, d = bridge_info.pop()
    flag = False
    if not visited[f]:
        visited[f] = True
        for i in range(len(distance_board[f])):
            if distance_board[f][i] != N * M:
                bridge_info.append([f, i, distance_board[f][i]])
    if not visited[s]:
        flag = True
        visited[s] = True
        for i in range(len(distance_board[s])):
            if distance_board[s][i] != N * M:
                bridge_info.append([s, i, distance_board[s][i]])
    if flag:
        result += d
    if False not in set(visited):
        break
    else:
        bridge_info.sort(key=lambda x:x[2], reverse=True)

if False in set(visited):
    print(-1)
else:
    print(result)