def main():
    r, c, k = map(int, input().split())
    r -= 1
    c -= 1
    board = [list(map(int, input().split())) for _ in range(3)]
    row = 3
    col = 3
    time = 0
    while True:
        if len(board) > r and len(board[r]) > c:
            if board[r][c] == k:
                break
        time += 1
        if time > 100:
            time = -1
            break
        if row >= col:
            max_col = 0
            for i in range(row):
                dic = {}
                for j in range(col):
                    if board[i][j] != 0:
                        if board[i][j] not in dic:
                            dic[board[i][j]] = 1
                        else:
                            dic[board[i][j]] += 1
                dic = dict(sorted(dic.items(), key = lambda x: (x[1], x[0])))
                new_row = []
                dic_keys = list(dic.keys())
                dic_values = list(dic.values())
                for j in range(len(dic_keys)):
                    new_row.append(dic_keys[j])
                    new_row.append(dic_values[j])
                max_col = max(max_col, len(new_row))
                board[i] = new_row
            col = max_col
            for i in range(row):
                row_len = len(board[i])
                if row_len < max_col:
                    for _ in range(max_col - row_len):
                        board[i].append(0)
        elif row < col:
            max_row = 0
            for i in range(col):
                dic = {}
                for j in range(row):
                    if board[j][i] != 0:
                        if board[j][i] not in dic:
                            dic[board[j][i]] = 1
                        else:
                            dic[board[j][i]] += 1
                dic = dict(sorted(dic.items(), key = lambda x: (x[1], x[0])))
                new_col = []
                dic_keys = list(dic.keys())
                dic_values = list(dic.values())
                for j in range(len(dic_keys)):
                    new_col.append(dic_keys[j])
                    new_col.append(dic_values[j])
                if len(board) > len(new_col):
                    for j in range(len(board) - len(new_col)):
                        board[len(board)-1 - j][i] = 0
                for j in range(len(new_col)):
                    if len(board)-1 < j:
                        board.append([0 for _ in range(col)])
                    board[j][i] = new_col[j]
                max_row = max(max_row, len(new_col))
            row = max_row
    print(time)
    return time


if __name__ == '__main__':
    main()