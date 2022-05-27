import sys
sys.setrecursionlimit(10**9)

def spread(N, board, min_time, spread_time, order, check):
    if min_time < spread_time:
        return min_time
    
    if spread_time == 0:
        zero = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    zero = 1
                    break
            if zero == 1:
                break
        if zero == 0:
            return spread_time
        board = [board[i][:] for i in range(len(board))]
    
    change = 0
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    new_check = []
    for i in range(len(check)):
        for j in range(4):
            y = check[i][0] + dy[j]
            x = check[i][1] + dx[j]
            if y >= 0 and y < N and x >= 0 and x < N:
                if board[y][x] == 0 or board[y][x] == 2:
                    change = 1
                    board[y][x] = order + 1
                    new_check.append((y,x))

    spread_time += 1
    zero = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                zero = 1
                break
        if zero == 1:
            break
    if change == 0 and zero == 1:
        return min_time
    elif zero == 0:
        min_time = min(min_time, spread_time)
        return min_time
    return spread(N, board, min_time, spread_time, order+1, new_check)
    

def search(i, j, N, M, board, active, min_time, virus):
    while i < N:
        while j < N:
            if board[i][j] == 2:
                board[i][j] = 3
                active += 1
                virus.append((i,j))
                if active < M:
                    y = i
                    x = j
                    if x == N-1:
                        y += 1
                        x = 0
                    else:
                        x += 1
                    min_time = search(y, x, N, M, board, active, min_time, virus)
                elif active == M:
                    min_time = spread(N, board, min_time, 0, 3, virus)
                active -= 1
                board[i][j] = 2
                virus.pop()
            j += 1
        j = 0
        i += 1
    return min_time


def main():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_time = search(0, 0, N, M, board, 0, N*N, [])
    if min_time == N*N:
        min_time = -1
    print(min_time)
    return min_time

if __name__ == '__main__':
    main()