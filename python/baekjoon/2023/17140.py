r, c, k = list(map(int, input().split()))
r -= 1
c -= 1
board = [list(map(int, input().split())) for _ in range(3)]

def row_calc(board):
    longest = 0
    row_len = len(board)
    col_len = len(board[0])
    for i in range(row_len):
        num_dict = {}
        for j in range(col_len):
            num = board[i][j]
            if num > 0:
                if num in num_dict:
                    num_dict[num] += 1
                else:
                    num_dict[num] = 1
        num_list = list(num_dict.items())
        num_list.sort(key = lambda x: (x[1], x[0]))
        num_list = list(map(list, num_list))
        num_list = sum(num_list, [])
        longest = max(longest, len(num_list))
        board.append(num_list)
    board = board[row_len:]
    for i in range(row_len):
        for _ in range(longest - len(board[i])):
            board[i].append(0)
    return board

def col_calc(board):
    longest = 0
    row_len = len(board)
    col_len = len(board[0])
    col_matrix = []
    for i in range(col_len):
        num_dict = {}
        for j in range(row_len):
            num = board[j][i]
            if num > 0:
                if num in num_dict:
                    num_dict[num] += 1
                else:
                    num_dict[num] = 1
        num_list = list(num_dict.items())
        num_list.sort(key = lambda x: (x[1], x[0]))
        num_list = list(map(list, num_list))
        num_list = sum(num_list, [])
        longest = max(longest, len(num_list))
        col_matrix.append(num_list)
    for i in range(col_len):
        for _ in range(longest - len(col_matrix[i])):
            col_matrix[i].append(0)
    board = [[0 for _ in range(col_len)] for _ in range(longest)]
    for i in range(longest):
        for j in range(col_len):
            board[i][j] = col_matrix[j][i]
    return board

def main():
    global r, c, k, board
    time = 0

    while time <= 100:
        if r < len(board) and c < len(board[0]) and board[r][c] == k:
            print(time)
            return time
        if len(board) >= len(board[0]):
            board = row_calc(board)
        else:
            board = col_calc(board)
        time += 1
    
    print(-1)
    return -1

if __name__ == '__main__':
    main()