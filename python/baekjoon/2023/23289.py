from collections import deque

R, C, K = list(map(int, input().split()))

# 위 오른 아래 왼
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

board = []
# 온풍기 위치
heater = []
# 온도 체크해야하는 곳
check_loca = []
for i in range(R):
    command = list(map(int, input().split()))
    # [위, 오른, 아래, 왼, 온도]
    row = []
    for j in range(C):
        if command[j] == 5:
            check_loca.append([i, j])
        elif command[j] != 0:
            # command => 1:오, 2:왼, 3:위, 4:아래 // d: 위 오른 아래 왼 순서
            d = 0
            if command[j] == 1:
                d = 1
            elif command[j] == 2:
                d = 3
            elif command[j] == 3:
                d = 0
            elif command[j] == 4:
                d = 2
            heater.append([i, j, d])
        row.append([0, 0, 0, 0, 0])
    board.append(row)

W = int(input())
for i in range(W):
    y, x, t = list(map(int, input().split()))
    y -= 1
    x -= 1
    if t == 0:
        board[y][x][0] = 1
        board[y-1][x][2] = 1
    else:
        board[y][x][1] = 1
        board[y][x+1][3] = 1


def heat(board, heater):
    global R, C, dy, dx

    for l in heater:
        visited = [[0 for _ in range(C)] for _ in range(R)]
        y, x, d = l
        y += dy[d]
        x += dx[d]
        # 온풍기 앞에 바로 벽이 있는 경우는 코드 수정해야함
        board[y][x][4] += 5
        visited[y][x] = 1
        queue = deque([[y, x, 4]])
        while len(queue) != 0:
            y, x, t = queue.popleft()
            if board[y][x][d] != 1:
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < R and 0 <= nx < C and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    board[ny][nx][4] += t
                    if t-1 > 0:
                        queue.append([ny, nx, t-1])

            side1 = d-1
            side2 = d+1
            back = d+2
            if side1 < 0:
                side1 += 4
            if side2 > 3:
                side2 -= 4
            if back > 3:
                back -= 4
            for side in [side1, side2]:
                if board[y][x][side] != 1:
                    ny = y + dy[d] + dy[side]
                    nx = x + dx[d] + dx[side]
                    if 0 <= ny < R and 0 <= nx < C and board[ny][nx][back] == 0 and visited[ny][nx] == 0:
                        visited[ny][nx] = 1
                        board[ny][nx][4] += t
                        if t-1 > 0:
                            queue.append([ny, nx, t-1])


def control(board):
    global R, C, dy, dx

    pm = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            for d in [1, 2]:
                ay = i + dy[d]
                ax = j + dx[d]
                if board[i][j][d] == 0 and 0 <= ay < R and 0 <= ax < C:
                    if board[i][j][4] < board[ay][ax][4]:
                        big = [ay, ax]
                        small = [i, j]
                    elif board[i][j][4] > board[ay][ax][4]:
                        big = [i, j]
                        small = [ay, ax]
                    else:
                        continue
                    num = (board[big[0]][big[1]][4] - board[small[0]][small[1]][4]) // 4
                    pm[big[0]][big[1]] -= num
                    pm[small[0]][small[1]] += num
    
    for i in range(R):
        for j in range(C):
            board[i][j][4] += pm[i][j]
            if i == 0 or i == R-1 or j == 0 or j == C-1:
                if board[i][j][4] != 0:
                    board[i][j][4] -= 1


def check(board, check_loca):
    global K

    result = True
    for l in check_loca:
        y, x = l
        if board[y][x][4] < K:
            result = False
            break

    return result


def main():
    global R, C, K, dy, dx, board, heater, check_loca

    cnt = 0
    while True:
        cnt += 1
        if cnt == 101:
            break
        heat(board, heater)
        control(board)
        if check(board, check_loca):
            break
        
    print(cnt)

if __name__ == '__main__':
    main()