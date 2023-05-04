global n, m, board, visited, result, maxnum
nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]

board = []
maxnum = 0
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    maxnum = max(maxnum, max(row))

visited = [[0 for _ in range(m)] for _ in range(n)]
result = 0

def check(y, x, depth, sumnum):
    global n, m, board, visited, result, maxnum

    if depth == 4:
        if result < sumnum:
            result = sumnum
        return 0

    if sumnum + maxnum * (4-depth) < result:
        return 0

    # 북 동 남 서
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny > n-1 or nx < 0 or nx > m-1 or visited[ny][nx] == 1:
            continue
        if depth == 2:
            visited[ny][nx] = 1
            check(y, x, depth+1, sumnum + board[ny][nx])
            visited[ny][nx] = 0
        visited[ny][nx] = 1
        check(ny, nx, depth+1, sumnum + board[ny][nx])
        visited[ny][nx] = 0
        


def main():
    global n, m, board, visited
    for i in range(n):
        for j in range(m):
            visited[i][j] = 1
            check(i, j, 1, board[i][j])
            visited[i][j] = 0


if __name__ == '__main__':
    main()
    print(result)
