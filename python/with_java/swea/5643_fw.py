tcCnt = int(input())

def fw(board, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if board[i][k] and board[k][j]:
                    board[i][j] = True

answer = []
for tc in range(1, tcCnt + 1):
    n = int(input())
    m = int(input())
    board = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        s, e = map(lambda x:x-1, map(int, input().split()))
        board[s][e] = True

    result = 0

    fw(board, n)
    for i in range(n):
        taller = 0
        smaller = 0
        for j in range(n):
            if board[i][j]:
                taller += 1
            if board[j][i]:
                smaller += 1
        if taller + smaller == n - 1:
            result += 1

    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)

print("\n".join(answer))