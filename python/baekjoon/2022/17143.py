from collections import deque

def main():
    R, C, M = map(int, input().split())
    board = [[deque([]) for _ in range(C)] for _ in range(R)]
    
    shark_location = []
    for i in range(M):
        r, c, s, d, z = map(int, input().split())
        board[r-1][c-1].append([s, d, z])
        shark_location.append((r-1, c-1))
    
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, 1, -1]

    shark_size = 0
    for i in range(C):
        # 한칸 옮겨서 상어잡기
        for j in range(R):
            if len(board[j][i]) != 0:
                shark_size += board[j][i][0][2]
                board[j][i] = deque([])
                shark_location.remove((j, i))
                break
        # 상어이동
        for k in range(len(shark_location)):
            y = shark_location[0][0]
            x = shark_location[0][1]
            shark_location.remove((y, x))
            shark_info = board[y][x].popleft()
            s = shark_info[0]
            d = shark_info[1]
            z = shark_info[2]
            if d == 1 or d == 2:
                s = s % (2*(R-1))
            elif d == 3 or d == 4:
                s = s % (2*(C-1))
            for _ in range(s):
                if y == 0 and d == 1:
                    d += 1
                elif y == R-1 and d == 2:
                    d -= 1
                if x == 0 and d == 4:
                    d -= 1
                elif x == C-1 and d == 3:
                    d += 1
                y = y + dy[d]
                x = x + dx[d]
            board[y][x].append([s, d, z])
            shark_location.append((y,x))
        # 동족상잔
        for l in range(R):
            for m in range(C):
                if len(board[l][m]) >= 2:
                    biggest = 0
                    index = 0
                    for n in range(len(board[l][m])):
                        if biggest < board[l][m][n][2]:
                            biggest = board[l][m][n][2]
                            index = n
                    board[l][m] = deque([board[l][m][index]])
        shark_location = list(set(shark_location))
    print(shark_size)
    return shark_size


if __name__ == '__main__':
    main()