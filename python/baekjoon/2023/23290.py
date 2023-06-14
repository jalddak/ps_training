M, S = list(map(int, input().split()))
board = [[[] for _ in range(4)] for _ in range(4)]

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(M):
    y, x, d = list(map(lambda x:x-1, list(map(int, input().split()))))
    board[y][x].append(d)

s_loca = list(map(lambda x:x-1, list(map(int, input().split()))))

# one step before smell
osbs = [[0 for _ in range(4)] for _ in range(4)]
tsbs = [[0 for _ in range(4)] for _ in range(4)]


def fishcopy(board):
    copy_board = []
    for i in range(4):
        copy_row = []
        for j in range(4):
            copy_row.append(board[i][j][:])
        copy_board.append(copy_row)
    
    return copy_board


def fishmove(board, s_loca, osbs, tsbs):
    global dy, dx
    
    move_board = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if len(board[i][j]) != 0:
                for k in range(len(board[i][j])):
                    d = board[i][j][k]
                    check = 0
                    for _ in range(8):
                        ny = i + dy[d]
                        nx = j + dx[d]
                        if 0 <= ny < 4 and 0 <= nx < 4 and osbs[ny][nx] == 0 and tsbs[ny][nx] == 0 and [ny, nx] != s_loca:
                            move_board[ny][nx].append(d)
                            check = 1
                            break
                        d -= 1
                        if d < 0:
                            d += 8
                    if check == 0:
                        move_board[i][j].append(d)

    return move_board


def dfs(board, y, x, depth, order, cnt, visited):
    # 상 좌 하 우
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    candidates = []
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            plus = 0
            if [ny, nx] not in visited:
                plus += len(board[ny][nx])
            if depth < 3:
                copy_visited = []
                for j in range(len(visited)):
                    copy_visited.append(visited[j][:])
                copy_visited.append([ny, nx])
                candidates.append(dfs(board, ny, nx, depth+1, order + str(i), cnt+plus, copy_visited))
            else:
                candidates.append([cnt+plus, order+str(i)])
    candidates.sort(key = lambda x: (-x[0], x[1]))
    return candidates[0]


def sharkmove(board, s_loca):
    # 상 좌 하 우
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    y, x = s_loca
    ds = dfs(board, y, x, 1, '', 0, [])[1]
    smell = [[0 for _ in range(4)] for _ in range(4)]
    for d in ds:
        d = int(d)
        y += dy[d]
        x += dx[d]
        if len(board[y][x]) != 0:
            smell[y][x] = 1
            board[y][x] = []
    
    s_loca = [y, x]
    return s_loca, smell


def smellcheck(smell, osbs, tsbs):
    for i in range(4):
        for j in range(4):
            tsbs[i][j] = osbs[i][j]
            osbs[i][j] = smell[i][j]


def main():
    global M, S, board, dy, dx, s_loca, osbs, tsbs

    for _ in range(S):
        # copy result
        cr = fishcopy(board)
        board = fishmove(board, s_loca, osbs, tsbs)
        s_loca, smell = sharkmove(board, s_loca)
        smellcheck(smell, osbs, tsbs)
        for i in range(4):
            for j in range(4):
                board[i][j] += cr[i][j]
    
    result = 0
    for i in range(4):
        for j in range(4):
            result += len(board[i][j])
    print(result)


if __name__ == '__main__':
    main()