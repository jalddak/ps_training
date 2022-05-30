from collections import deque

def check(board, new_board, n, m, N, M, check_same):
    if n + 1 <= N:
        if board[n][m] == board[n+1][m]:
            new_board[n][m] = 0
            new_board[n+1][m] = 0
            check_same = 1
    right = m + 1
    if right > M-1:
        right = 0
    if board[n][m] == board[n][right]:
        new_board[n][m] = 0
        new_board[n][right] = 0
        check_same = 1
    return check_same


def main():
    N, M, T = map(int, input().split())
    board = [deque([0 for _ in range(M)])]
    for _ in range(N):
        board.append(deque(list(map(int, input().split()))))
    rotate_methods = [list(map(int, input().split())) for _ in range(T)]

    for i in range(len(rotate_methods)):
        x, d, k = rotate_methods[i][0], rotate_methods[i][1], rotate_methods[i][2]
        for j in range(x, N+1, x):
            if d == 0:
                for _ in range(k):
                    board[j].appendleft(board[j].pop())
            elif d == 1:
                for _ in range(k):
                    board[j].append(board[j].popleft())
        
        new_board = [deque(list(board[j])[:]) for j in range(N+1)]
        check_same = 0
        sum_num = 0
        count = 0

        for n in range(1, N+1):
            for m in range(M):
                if board[n][m] != 0:
                    check_same = check(board, new_board, n, m, N, M, check_same)
                    sum_num += board[n][m]
                    count += 1

        if check_same == 0:
            if count != 0:
                mean = float(sum_num) / count
            for n in range(1, N+1):
                for m in range(M):
                    if board[n][m] != 0:
                        if board[n][m] < mean:
                            board[n][m] += 1
                        elif board[n][m] > mean:
                            board[n][m] -= 1
        else:
            board = new_board

    last_sum = 0
    for n in range(1, N+1):
        for m in range(M):
            if board[n][m] != 0:
                check_same = check(board, new_board, n, m, N, M, check_same)
                last_sum += board[n][m]
    print(last_sum)
    return last_sum


if __name__ == '__main__':
    main()

