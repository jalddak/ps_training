dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]

fishes = [[] for _ in range(16)]
board = [[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    command = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = command[j*2]
        fishes[command[j*2]-1] = [i, j, command[j*2+1]]

def fish_move(board, fishes):
    global dy, dx
    for i in range(len(fishes)):
        fish = fishes[i]
        if len(fish) == 0:
            continue
        y, x, d = fish
        ny = y + dy[d]
        nx = x + dx[d]
        while ny >= 4 or ny < 0 or nx >= 4 or nx < 0 or board[ny][nx] == 20:
            d += 1
            if d == 9:
                d = 1
            ny = y + dy[d]
            nx = x + dx[d]

        fish_num = board[y][x]
        board[y][x] = 0
        if board[ny][nx] != 0:
            board[y][x] = board[ny][nx]
            fishes[board[y][x]-1] = [y, x, fishes[board[y][x]-1][2]]
        board[ny][nx] = fish_num
        fishes[fish_num-1] = [ny, nx, d]


def shark_move(board, shark, fishes, num):
    global dy, dx

    fish_move(board, fishes)
    y, x, d = shark
    ny = y + dy[d]
    nx = x + dx[d]

    nums = [num]

    while 0 <= ny < 4 and 0 <= nx < 4:
        if board[ny][nx] != 0:
            board_copy = []
            for i in range(4):
                board_copy.append(board[i][:])
            fishes_copy = fishes[:]
            feed_num = board_copy[ny][nx]
            board_copy[ny][nx] = 20
            board_copy[y][x] = 0
            sub_shark = [ny, nx, fishes_copy[feed_num-1][2]]
            fishes_copy[feed_num-1] = []
            nums.append(shark_move(board_copy, sub_shark, fishes_copy, num + feed_num))
        ny += dy[d]
        nx += dx[d]

    return max(nums)

def main():
    global dy, dx, fishes, board

    feed_num = board[0][0]
    board[0][0] = 20
    shark = [0, 0, fishes[feed_num-1][2]]
    fishes[feed_num-1] = []

    result = shark_move(board, shark, fishes, feed_num)
    print(result)


if __name__ == '__main__':
    main()