N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0]


def recursion(term, sy, sx):
    global board
    num_l = set([])
    for y in range(sy, sy+term):
        for x in range(sx, sx+term):
            num_l.add(board[y][x])
            if len(num_l) != 1:
                break
        if len(num_l) != 1:
            break
    if len(num_l) != 1:
        term //= 2
        recursion(term, sy, sx)
        recursion(term, sy, sx+term)
        recursion(term, sy+term, sx)
        recursion(term, sy+term, sx+term)
    else:
        for i in range(2):
            if i in num_l:
                result[i] += 1

recursion(N, 0, 0)
for n in result:
    print(n)