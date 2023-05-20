import sys
sys.setrecursionlimit(10**6)

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
union = [[0 for _ in range(n)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = 0

def dfs(num, y, x):
    global n, l, r, board, union, dy, dx, result
    current = board[y][x]
    check = 0
    for k in range(4):
        ay = y + dy[k]
        ax = x + dx[k]
        if 0 <= ay < n and 0 <= ax < n:
            around = board[ay][ax]
            if l <= abs(current - around) <= r:
                if union[ay][ax] == 0:
                    union[y][x] = num
                    union[ay][ax] = num
                    dfs(num, ay, ax)
                    check = 1
    return check

def move():
    global n, l, r, board, union, dy, dx, result
    while True:
        # 연합 만드는 과정
        num = 1
        check = 0
        for i in range(n):
            for j in range(n):
                if union[i][j] == 0:
                    open = dfs(num, i, j)
                    if open == 1:
                        check = 1
                    num += 1
        if check == 0:
            break

        # 인구 분배 과정
        udict = {}
        for i in range(n):
            for j in range(n):
                num = union[i][j]
                if num != 0:
                    if num not in udict:
                        udict[num] = [board[i][j]]
                    else:
                        udict[num].append(board[i][j])

        for i in udict.keys():
            udict[i] = sum(udict[i]) // len(udict[i])

        for i in range(n):
            for j in range(n):
                num = union[i][j]
                if num != 0:
                    board[i][j] = udict[num]

        result += 1
        union = [[0 for _ in range(n)] for _ in range(n)]

if __name__ == '__main__':
    move()
    print(result)