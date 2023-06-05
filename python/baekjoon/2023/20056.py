N, M, K = list(map(int, input().split()))

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    board[r-1][c-1].append([m, s, d])


def move(board):
    global N, dy, dx
    result = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            while len(board[i][j]) != 0:
                m, s, d = board[i][j].pop()
                y, x, = i, j
                for _ in range(s):
                    y += dy[d]
                    x += dx[d]
                    if y >= N:
                        y -= N
                    elif y < 0:
                        y += N
                    if x >= N:
                        x -= N
                    elif x < 0:
                        x += N
                    
                result[y][x].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(result[i][j]) >= 2:
                m = 0
                s = 0
                ds = []
                for fb in result[i][j]:
                    m += fb[0]
                    s += fb[1]
                    ds.append(fb[2])
                result[i][j] = []
                m = m // 5
                if m == 0:
                    continue
                s = s // len(ds)
                if len(set(map(lambda x:x%2, ds))) == 1:
                    ds = [0, 2, 4, 6]
                else:
                    ds =  [1, 3, 5, 7]
                for d in ds:
                    result[i][j].append([m, s, d])

    return result


def main():
    global N, M, K, board, dy, dx
    for _ in range(K):
        board = move(board)
    
    result = 0
    for i in range(N):
        for j in range(N):
            for k in range(len(board[i][j])):
                result += board[i][j][k][0]
    print(result)
    

if __name__ == '__main__':
    main()
