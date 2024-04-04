def bingo_check(line, bingo_type):
    line = set(line)
    if len(line) == 1 and '.' not in line:
        sign = line.pop()
        if sign in bingo_type:
            bingo_type[sign] += 1
    return

def solution(board):
    answer = -1
    board = list(map(list, board))
    bingo_type = {'O':0, 'X':0}
    ocnt = 0
    xcnt = 0
    for i in range(3):
        row = board[i]
        col = [board[j][i] for j in range(3)]
        bingo_check(row, bingo_type)
        bingo_check(col, bingo_type)
        for j in range(3):
            if board[i][j] == 'O':
                ocnt += 1
            elif board[i][j] == 'X':
                xcnt += 1
            if i == 1 and j == 1:
                lcross = [board[i][j], board[i-1][j-1], board[i+1][j+1]]
                rcross = [board[i][j], board[i+1][j-1], board[i-1][j+1]]
                bingo_check(lcross, bingo_type)
                bingo_check(rcross, bingo_type)
    
    if (bingo_type['O'] > 0 and bingo_type['X'] > 0) or (bingo_type['O'] == 1 and ocnt == xcnt) or (bingo_type['X'] == 1 and ocnt > xcnt) or ocnt < xcnt or ocnt - xcnt > 1:
        answer = 0
    else:
        answer = 1
    return answer