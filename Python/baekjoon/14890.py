# 파이썬 알게 된 것 : abs(n) <- 모듈이 필요없는 절대값으로 값을 바꿔주는 파이썬 내장함수

def main():
    N, L = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        board_row = list(map(int, input().split()))
        for j in range(N):
            board[i][j] = board_row[j]

    count = 0
    for i in range(N):
        not_count = 0
        now_height = board[i][0]
        stack = 1
        for j in range(1, N):
            if abs(board[i][j] - now_height) > abs(1):
                not_count = 1
                break
            if board[i][j] == now_height:
                stack += 1
            elif board[i][j] < now_height:
                if stack < 0:
                    not_count = 1
                    break
                else:
                    now_height = board[i][j]
                    stack = -L + 1
            elif board[i][j] > now_height:
                if stack < L:
                    not_count = 1
                    break
                else:
                    now_height = board[i][j]
                    stack = 1

        if not_count == 0 and stack >= 0:
            count += 1
    
    for j in range(N):
        not_count = 0
        now_height = board[0][j]
        stack = 1
        for i in range(1, N):
            if abs(board[i][j] - now_height) > abs(1):
                not_count = 1
                break
            if board[i][j] == now_height:
                stack += 1
            elif board[i][j] < now_height:
                if stack < 0:
                    not_count = 1
                    break
                else:
                    now_height = board[i][j]
                    stack = -L + 1
            elif board[i][j] > now_height:
                if stack < L:
                    not_count = 1
                    break
                else:
                    now_height = board[i][j]
                    stack = 1
            
        if not_count == 0 and stack >= 0:
            count += 1

    print(count)
    return count

if __name__ == '__main__':
    main()
