n, m, k = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

# 위 아래 왼 오
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

direction = list(map(lambda x: x-1,list(map(int, input().split()))))
shark_info = {}

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            board[i][j] = []
        else:
            shark_info[board[i][j]] = [i, j, direction[board[i][j]-1]]
            board[i][j] = [board[i][j], k]

# direction_rank
dr = [[list(map(lambda x: x-1, list(map(int, input().split())))) for _ in range(4)] for _ in range(m)]
dr.insert(0, [])


def move(board, shark_info, dr):
    global n, m, k, dy, dx

    for num in shark_info:
        y, x, d = shark_info[num]
        rank = dr[num][d]
        check = False
        for r in rank:
            ny = y + dy[r]
            nx = x + dx[r]
            if 0 <= ny < n and 0 <= nx < n and len(board[ny][nx]) == 0:
                check = True
                nd = r
                break
        if check == False:
            for r in rank:
                ny = y + dy[r]
                nx = x + dx[r]
                if 0 <= ny < n and 0 <= nx < n and board[ny][nx][0] == num:
                    nd = r
                    break
        shark_info[num] = [ny, nx, nd]


def delete(board):
    global n
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) != 0:
                board[i][j][1] -= 1
                if board[i][j][1] == 0:
                    board[i][j] = []


def spread(board, shark_info):
    global k

    nums = list(shark_info.keys())
    for num in nums:
        if num in shark_info:
            y, x, d = shark_info[num]
            if len(board[y][x]) == 0:
                board[y][x] = [num, k]
            elif board[y][x][0] < num:
                del shark_info[num]
            elif board[y][x][0] == num:
                board[y][x] = [num, k]
            else:
                del shark_info[board[y][x][0]]
                board[y][x] = [num, k]


def main():
    global n, m, k, dy, dx, board, shark_info, dr

    time = 0
    while len(shark_info) != 1 and time <= 1000:
        move(board, shark_info, dr)
        delete(board)
        spread(board, shark_info)
        time += 1
    if time > 1000:
        time = -1
    print(time)


if __name__ == '__main__':
    main()