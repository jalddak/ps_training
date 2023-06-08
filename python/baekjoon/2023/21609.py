from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]


def big_delete(board):
    global N, M, dy, dx

    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    rainbow = 0
    loca = []
    deletes = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and board[i][j] != -1 and board[i][j] != -10 and visited[i][j] == 0:
                queue = deque([[i, j]])
                color = board[i][j]
                visited[i][j] = 1
                temp_cnt = 1
                temp_rainbow = 0
                # temp delete candidate
                tdc = [[i, j]]
                while len(queue) != 0:
                    y, x = queue.popleft()
                    for k in range(4):
                        ay = y + dy[k]
                        ax = x + dx[k]
                        if 0 <= ay < N and 0 <= ax < N and visited[ay][ax] == 0:
                            if board[ay][ax] == 0:
                                temp_rainbow += 1
                            elif board[ay][ax] != color:
                                continue
                            temp_cnt += 1
                            queue.append([ay, ax])
                            visited[ay][ax] = 1
                            tdc.append([ay, ax])

                for d in tdc:
                    y, x = d
                    if board[y][x] == 0:
                        visited[y][x] = 0
                if len(tdc) < 2:
                    continue

                check = 0

                if temp_cnt > cnt:
                    check = 1
                elif temp_cnt == cnt and temp_rainbow > rainbow:
                    check = 1
                elif temp_cnt == cnt and temp_rainbow == rainbow and (len(loca) == 0 or i > loca[0]):
                    check = 1
                elif temp_cnt == cnt and temp_rainbow == rainbow and i == loca[0] and j > loca[1]:
                    check = 1

                if check == 1:
                    cnt = temp_cnt
                    rainbow = temp_rainbow
                    loca = [i, j]
                    deletes = tdc

    for d in deletes:
        y, x = d
        # -10 는 빈칸을 의미
        board[y][x] = -10

    return cnt ** 2


def gravity_on(board):
    global N, dy

    for i in range(N):
        for j in range(N-2, -1, -1):
            if board[j][i] != -1 and board[j][i] != -10:
                y = j
                while 0 <= y+1 < N and board[y+1][i] == -10:
                    board[y+1][i] = board[y][i]
                    board[y][i] = -10
                    y += 1


def rotate(board):
    global N

    rotating = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotate_j = N - j - 1
            rotating[rotate_j][i] = board[i][j]
    
    return rotating

def main():
    global N, M, dy, dx, board
    
    score = 0
    while True:
        # 가장 큰 블록 찾아서 삭제
        plus = big_delete(board)
        if plus == 0:
            break
        score += plus
        # 중력 온
        gravity_on(board)
        # 반시계 방향 회전
        board = rotate(board)
        # 중력 온
        gravity_on(board)

    print(score)




if __name__ == '__main__':
    main()