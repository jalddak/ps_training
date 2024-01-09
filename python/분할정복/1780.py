N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0, 0]
indexMap = {-1: 0, 0: 1, 1: 2}

def recursion(n, y, x):
    if n == 1:
        return board[y][x]
    piece = n // 3
    dy = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dx = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    check = []
    for d in range(9):
        ny = y + dy[d]*piece
        nx = x + dx[d]*piece
        check.append(recursion(piece, ny, nx))
    
    if len(set(check)) == 1 and check[0] != 2:
        return check[0]
    
    for n in check:
        if n != 2:
            result[indexMap[n]] += 1
    return 2

calc = recursion(N, 0, 0)
if calc != 2:
    result[indexMap[calc]] += 1

for r in result:
    print(r)

