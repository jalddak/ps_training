n = int(input())
# x, y, d, g
curves = [list(map(int, input().split())) for _ in range(n)]

def move(x, y, d):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    nx = x + dx[d]
    ny = y + dy[d]

    return [nx, ny]

# 기준점 - 비교점 ( x 차이는 기준점 y에 빼주고, y 차이는 기준점 x에 더해준다 )
def rotate(start, end, curve):
    next_end = []
    ncurve = curve[:]
    for c in curve:
        rc = [end[0] + (end[1] - c[1]), end[1] - (end[0] - c[0])]
        if c[0] == start[0] and c[1] == start[1]:
            next_end = rc
            continue
        ncurve.append(rc)
    ncurve.append(end)
    return ncurve, next_end

def check(board):
    global result
    result = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
                result += 1

def main():
    complete = []
    board = [[ 0 for _ in range(101)] for _ in range(101)]
    for c in curves:
        x, y, d, g = c[0], c[1], c[2], c[3]
        start = [x,y]
        curve = [[x,y]]
        end = move(x, y, d)
        for _ in range(g):
            curve, end = rotate(start, end, curve)
        curve.append(end)
        complete += curve
        for c in complete:
            board[c[1]][c[0]] = 1
    check(board)


if __name__ == '__main__':
    main()
    print(result)