def make_board():
    row, col = map(int, input().split())
    board = [[0 for _ in range(col)] for _ in range(row)]
    virus = []
    for i in range(row):
        board_row = list(map(int, input().split()))
        for j in range(col):
            board[i][j] = board_row[j]
            if board[i][j] == 2:
                virus.append([i,j])
    return board, virus

t = 0
def spread(board, y, x):
    global t
    t += 1
    print(t)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for k in range(4):
        after_y = y + dy[k]
        after_x = x + dx[k]
        if after_y >= 0 and after_y < len(board) and after_x >= 0 and after_x < len(board[0]):
            if board[after_y][after_x] == 0:
                board[after_y][after_x] = 2
                spread(board, after_y, after_x)
    

def make_wall(board, virus, num, before_visited):
    num += 1
    visited = before_visited[:]
    safe = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0 and [i,j] not in visited and [i,j] not in before_visited:
                board[i][j] = 1
                visited.append([i,j])
                if num != 3:
                    safe = max(safe, make_wall(board, virus, num, visited))
                else:
                    board_copy = []
                    for c in range(len(board)):
                        board_row_copy = board[c][:]
                        board_copy.append(board_row_copy)
                    for k in range(len(virus)):
                        spread(board_copy, virus[k][0], virus[k][1])
                    safe_candidate = 0
                    for a in range(len(board)):
                        for b in range(len(board[a])):
                            if board_copy[a][b] == 0:
                                safe_candidate += 1
                    safe = max(safe, safe_candidate)
                board[i][j] = 0
    return safe


def main():
    board, virus = make_board()
    safe = make_wall(board, virus, 0, [])
    print(safe)
    return safe

if __name__ == '__main__':
    main()