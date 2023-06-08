N, M = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
moving = [list(map(int, input().split())) for _ in range(M)]

cloud = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N-2, N):
    for j in range(2):
        cloud[i][j] = 1

dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cdy = [-1, 1, -1, 1]
cdx = [-1, 1, 1, -1]


def move(cloud, d, s):
    global N, dy, dx

    copy = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == 1:
                y, x = i, j
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
                copy[y][x] = 1
    return copy


def rain(cloud, board):
    global N

    increase = []
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == 1:
                board[i][j] += 1
                # 구름이 모두 사라진다.
                cloud[i][j] = 0
                increase.append([i, j])
    return increase


def copy_water(board, increase):
    global N, cdy, cdx

    visited = [[0 for _ in range(N)] for _ in range(N)]
    for loca in increase:
        y, x = loca
        visited[y][x] = 1
        for i in range(4):
            cy = y + cdy[i]
            cx = x + cdx[i]
            # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
            # 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
            # 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
            if 0 <= cy < N and 0 <= cx < N and board[cy][cx] > 0:
                board[y][x] += 1
    return visited


def make_cloud(board, cloud, visited):
    global N

    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and visited[i][j] != 1:
                cloud[i][j] = 1
                board[i][j] -= 2


def main():
    global N, M, board, moving, cloud, dy, dx, cdy, cdx

    for i in range(M):
        d, s = moving[i]
        # 모든 구름이 di 방향으로 si칸 이동한다.
        cloud = move(cloud, d, s)
        # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        increase = rain(cloud, board)
        # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 
        visited = copy_water(board, increase)
        # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
        make_cloud(board, cloud, visited)
    
    result = 0
    for i in range(N):
        for j in range(N):
            result += board[i][j]
    print(result)


if __name__ == '__main__':
    main()