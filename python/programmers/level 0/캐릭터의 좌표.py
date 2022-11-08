def solution(keyinput, board):
    row_len = (board[0] - 1) // 2
    col_len = (board[1] - 1) // 2
    answer = [0, 0]
    for key in keyinput:
        if key == 'left':
            if 0 - answer[0] < row_len:
                answer[0] -= 1
        elif key == 'right':
            if answer[0] < row_len:
                answer[0] += 1
        elif key == 'up':
            if answer[1] < col_len:
                answer[1] += 1
        else:
            if 0 - answer[1] < col_len:
                answer[1] -= 1
    return answer