# 이 문제로 배운 점: 백준 챗점 프로그램에서 python3 보다 pypy3 가 더 빠르다.

def make_board():
    size = list(map(int, input().split()))
    board = [[0 for _ in range(size[1])] for _ in range(size[0])]
    for i in range(size[0]):
        row = list(map(int, input().split()))
        for j in range(size[1]):
            board[i][j] = row[j]
    return board


def biggest_poly_dfs(board, y, x, number, count, exception):
    if count >= 4:
        return number
    count += 1
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    candidates = []
    for i in range(4):
        if i == exception:
            continue

        y_c = y + dy[i]
        x_c = x + dx[i]
        if y_c < 0 or y_c > len(board) - 1 or x_c < 0 or x_c > len(board[0]) - 1:
            continue

        num_c = number + board[y_c][x_c]
        exception_c = i + 2
        if exception_c >= 4:
            exception_c -= 4

        candidates.append(biggest_poly_dfs(board, y_c, x_c, num_c, count, exception_c))
    
    return max(candidates)


def biggest_poly_around(board, y, x):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    around = []
    around_num = 0
    for i in range(4):
        y_c = y + dy[i]
        x_c = x + dx[i]
        if y_c < 0 or y_c > len(board) - 1 or x_c < 0 or x_c > len(board[0]) - 1:
            continue
        around.append(board[y_c][x_c])
        around_num += board[y_c][x_c]
    if len(around) == 4:
        around_num -= min(around)
    return board[y][x] + around_num
        

def main():
    board = make_board()
    biggest = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            candidate_dfs = biggest_poly_dfs(board, i, j, board[i][j], 1, 4)
            candidate_around = biggest_poly_around(board, i, j)
            candidate = max(candidate_dfs, candidate_around)
            if biggest < candidate:
                biggest = candidate
    print(biggest)
    return biggest


if __name__ == '__main__':
    main()