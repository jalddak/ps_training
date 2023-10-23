N, M = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]

def check_change(starter):
    copy_board = []
    for i in range(N):
        copy_board.append(board[i][:])
    changed = [[0 for _ in range(M)] for _ in range(N)]
    if copy_board[0][0] != starter:
        copy_board[0][0] = starter
        changed[0][0] = 1
    for i in range(1, N):
        if copy_board[i][0] == copy_board[i-1][0]:
            copy_board[i][0] = 'W' if copy_board[i][0] == 'B' else 'B'
            changed[i][0] = 1
    
    for i in range(N):
        for j in range(1, M):
            if copy_board[i][j] == copy_board[i][j-1]:
                copy_board[i][j] = 'W' if copy_board[i][j] == 'B' else 'B'
                changed[i][j] = 1
    
    return changed
    
B_changed = check_change('B')
W_changed = check_change('W')

def min_calc(changed):
    min_sum = 64
    for i in range(N-7):
        for j in range(M-7):
            col_row_sum = 0
            for r in range(i, i+8):
                row_sum = sum(changed[r][j:j+8])
                col_row_sum += row_sum
            min_sum = min(min_sum, col_row_sum)
    
    return min_sum

B_min = min_calc(B_changed)
W_min = min_calc(W_changed)

print(min(B_min, W_min))