import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, list(input())[:-1])) for _ in range(N)]

def recursion(n, y, x):
    if n == 1:
        return board[y][x]
    
    half = n//2
    dy = [0, 0, 1, 1]
    dx = [0, 1, 0, 1]
    check = []
    for d in range(4):
        check.append(recursion(half, y+dy[d]*half, x+dx[d]*half))
    if len(set(check)) == 1:
        if check[0] == 0:
            return 0
        elif check[0] == 1:
            return 1
    return "(" + "".join(map(str, check)) + ")"

print(recursion(N, 0, 0))