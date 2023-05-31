from collections import deque

green = deque([[0 for _ in range(4)] for _ in range(6)])
blue = deque([[0 for _ in range(4)] for _ in range(6)])

n = int(input())
order = [list(map(int, input().split())) for _ in range(n)]

def put(t, x, board):
    check = []
    if t == 1:
        for i in range(6):
            if board[i][x] != 0:
                break
            check = [[i, x]]
    elif t == 2:
        for i in range(6):
            if board[i][x] != 0 or board[i][x+1] != 0:
                break
            check = [[i, x], [i, x+1]]

    elif t == 3:
        for i in range(5):
            if board[i+1][x] != 0:
                break
            check = [[i, x], [i+1, x]]

    for i, j in check:
        board[i][j] = 1

def check(board):
    plus = []
    for i in range(2, 6):
        if board[i] == [1, 1, 1, 1]:
            plus.append(i)
    plus.reverse()
    for i in plus:
        board = list(board)
        board.pop(i)
        board = deque(board)
    for _ in range(len(plus)):
        board.appendleft([0, 0, 0, 0])

    for _ in range(2):
        if 1 in board[1]:
            board.pop()
            board.appendleft([0, 0, 0, 0])
    
    return board, len(plus)

def count(board):
    cnt = 0
    for i in range(2, 6):
        for j in range(4):
            if board[i][j] == 1:
                cnt += 1

    return cnt

def main():
    global n, order, green, blue

    score = 0
    for t, y, x in order:
        put(t, x, green)
        if t == 2:
            t += 1
        elif t == 3:
            t -= 1
        put(t, y, blue)
        green, plus = check(green)
        score += plus
        blue, plus = check(blue)
        score += plus
    print(score)

    cnt = 0
    cnt += count(green)
    cnt += count(blue)
    print(cnt)


if __name__ == '__main__':
    main()