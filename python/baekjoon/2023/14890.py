first_row = list(map(int, input().split()))
n = first_row[0]
l = first_row[1]

board = [list(map(int, input().split())) for _ in range(n)]
result = 0

def row_check(y):
    global n, l, result
    # -1 0 1 : 앞 x 뒤
    check = 0
    stack = 1
    for i in range(1, n):
        if board[y][i-1] == board[y][i]:
            stack += 1
        elif board[y][i-1] - board[y][i] == 1:
            if check != 0:
                return False
            check = -1
            stack = 1
        elif board[y][i-1] - board[y][i] == -1:
            check = 1
            if stack < l:
                return 0
            check = 0
            stack = 1
        else:
            return 0
        if check == -1 and stack == l:
            stack = 0
            check = 0
    if check != 0:
        return 0
    else:
        result += 1


def col_check(x):
    global n, l, result
    # -1 0 1 : 앞 x 뒤
    check = 0
    stack = 1
    for i in range(1, n):
        if board[i-1][x] == board[i][x]:
            stack += 1
        elif board[i-1][x] - board[i][x] == 1:
            if check != 0:
                return False
            check = -1
            stack = 1
        elif board[i-1][x] - board[i][x] == -1:
            check = 1
            if stack < l:
                return 0
            check = 0
            stack = 1
        else:
            return 0
        if check == -1 and stack == l:
            stack = 0
            check = 0
    if check != 0:
        return 0
    else:
        result += 1


def main():
    global n
    for i in range(n):
        row_check(i)
        col_check(i)
    print(result)


if __name__ == '__main__':
    main()
