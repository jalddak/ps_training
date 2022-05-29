from collections import deque
import sys
sys.setrecursionlimit(10**9)

def spread(N, board, min_time, spread_time, check, zero_count):
    if min_time < spread_time:
        return min_time
    
    if spread_time == 0:
        board = [board[i][:] for i in range(len(board))]
        check = deque(list(check)[:])
    
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    while True:
        for _ in range(len(check)):
            c = check.popleft()
            for i in range(4):
                y = c[0] + dy[i]
                x = c[1] + dx[i]
                if y >= 0 and y < N and x >= 0 and x < N:
                    if board[y][x] == 0 or board[y][x] == 2:
                        if board[y][x] == 0:
                            zero_count -= 1
                        board[y][x] = 3
                        check.append((y,x))
        spread_time += 1
        if zero_count == 0:
            min_time = min(min_time, spread_time)
        elif len(check) != 0 and zero_count > 0:
            continue
        return min_time
    

def search(virus, index, N, M, board, active, min_time, check, zero_count):
    for i in range(index, len(virus)):
        active += 1
        if len(virus) - 1 - i < M - active:
            return min_time
        y, x = virus[i][0], virus[i][1]
        board[y][x] = 3
        check.append((y,x))
        if active < M:
            min_time = search(virus, i+1, N, M, board, active, min_time, check, zero_count)
        elif active == M:
            min_time = spread(N, board, min_time, 0, check, zero_count)
        check.pop()
        board[y][x] = 2
        active -= 1
    return min_time


def main():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    virus = []
    zero_count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                virus.append((i,j))
            elif board[i][j] == 0:
                zero_count += 1
    if zero_count == 0:
        min_time = 0
    else:
        min_time = search(virus, 0, N, M, board, 0, N*N, deque([]), zero_count)
        if min_time == N*N:
            min_time = -1
    print(min_time)
    return min_time

if __name__ == '__main__':
    main()