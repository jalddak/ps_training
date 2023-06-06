N, Q = list(map(int, input().split()))
#board length
bl = 2 ** N
board = [list(map(int, input().split())) for _ in range(bl)]
Ls = list(map(int, input().split()))


def rotate(board, start, length):
    y, x = start
    sboard = []
    for i in range(y, y + length):
        sboard.append(board[i][x:x+length])
    
    copy = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        rotate_i = (length-1) - i
        for j in range(length):
            copy[j][rotate_i] = sboard[i][j]
    
    for i in range(length):
        for j in range(length):
            board[i+y][j+x] = copy[i][j]


def check(board):
    global bl

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    total = 0
    delete = []
    for i in range(bl):
        for j in range(bl):
            if board[i][j] != 0:
                around = 0
                for k in range(4):
                    y = i + dy[k]
                    x = j + dx[k]
                    if 0 <= y < bl and 0 <= x < bl and board[y][x] != 0:
                        around += 1
                if around < 3:
                    delete.append([i, j])
                total += board[i][j]
    total -= len(delete)
    for y, x in delete:
        board[y][x] -= 1
    
    return total
    
# dfs 로 풀어보려했으나 재귀를 너무 많이해서 안됨
# def bigcount(board, visited, y, x):
#     global bl

#     dy = [-1, 0, 1, 0]
#     dx = [0, 1, 0, -1]
#     visited[y][x] = 1

#     size = board[y][x]
#     cnt = 1

#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= ny < bl and 0 <= nx < bl and visited[ny][nx] == 0 and board[ny][nx] != 0:
#             ps, pc = bigcount(board, visited, ny, nx)
#             size += ps
#             cnt += pc

#     return size, cnt

def bfs(board, visited, y, x):
    global bl

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited[y][x] = 1
    size = 1
    queue = [[y, x]]
    while len(queue) != 0:
        y, x = queue.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < bl and 0 <= nx < bl and visited[ny][nx] == 0 and board[ny][nx] != 0:
                size += 1
                visited[ny][nx] = 1
                queue.append([ny, nx])
    return size


def bigcount(board):
    global bl

    visited = [[0 for _ in range(bl)] for _ in range(bl)]
    max_size = 0
    for i in range(bl):
        for j in range(bl):
            if visited[i][j] == 0 and board[i][j] != 0:
                size = bfs(board, visited, i, j)
                if max_size < size:
                    max_size = size
    
    return max_size



def main():
    global N, Q, bl, board, Ls

    remain = 0
    for i in range(Q):
        L = Ls[i]
        sbl = 2 ** L
        # 작은 격자 간격(?)
        interval = bl // sbl
        for j in range(interval):
            for k in range(interval):
                y = j * sbl
                x = k * sbl
                rotate(board, [y, x], sbl)

        remain = check(board)

    print(remain)
    cnt = bigcount(board)
    if cnt == 1:
        cnt = 0
    print(cnt)


if __name__ == '__main__':
    main()