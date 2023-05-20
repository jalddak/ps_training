from collections import deque

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
union = [[0 for _ in range(n)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = 0
while True:
    check = 0
    num = 0
    avg = {}
    for i in range(n):
        for j in range(n):
            if union[i][j] == 0:
                num += 1
                cnt = 0
                population = 0
                queue = deque([[i, j]])
                while len(queue) != 0:
                    y, x = queue.popleft()
                    current = board[y][x]
                    for k in range(4):
                        ay = y + dy[k]
                        ax = x + dx[k]
                        if 0 <= ay < n and 0 <= ax < n:
                            around = board[ay][ax]
                            if l <= abs(current - around) <= r:
                                check = 1
                                if union[ay][ax] == 0:
                                    queue.append([ay, ax])
                                    if union[y][x] == 0:
                                        union[y][x] = num
                                        population += board[y][x]
                                        cnt += 1
                                    union[ay][ax] = num
                                    population += board[ay][ax]
                                    cnt += 1
                if cnt != 0:
                    avg[num] = population // cnt
    if check == 0:
        break
    for i in range(n):
        for j in range(n):
            num = union[i][j]
            if num != 0:
                board[i][j] = avg[num]
    union = [[0 for _ in range(n)] for _ in range(n)]
    result += 1
print(result)