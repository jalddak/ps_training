# import sys
# sys.stdin = open('./python/with_java/swea/input.txt', 'r')
# sys.stdout = open('./python/with_java/swea/output.txt', 'w')

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cmdToIdx = {'U' : 0, 'R' : 1, 'D' : 2, 'L' : 3}
cmdToChar = {'U' : '^', 'R' : '>', 'D' : 'v', 'L' : '<'}
charToIdx = {'^':0, '>':1, 'v':2, '<':3}

def solution(h, w, board, n, cmds):
    y, x = -1, -1
    for i in range(h):
        for j in range(w):
            if board[i][j] in set(cmdToChar.values()):
                y, x = i, j
                break
    for cmd in cmds:
    
        if cmd != 'S':
            ny = y + dy[cmdToIdx[cmd]]
            nx = x + dx[cmdToIdx[cmd]]
            board[y][x] = cmdToChar[cmd]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if board[ny][nx] == '.':
                board[y][x] = '.'
                board[ny][nx] = cmdToChar[cmd]
                y, x = ny, nx

        else:
            sy = y
            sx = x
            while True:
                sy += dy[charToIdx[board[y][x]]]
                sx += dx[charToIdx[board[y][x]]]
                if sy < 0 or sy >= h or sx < 0 or sx >= w or board[sy][sx] == "#":
                    break
                if board[sy][sx] == "*":
                    board[sy][sx] = '.'
                    break
    
    return board


tcCnt = int(input())

sb = ""
for tc in range(1, tcCnt+1):
    sb += "#" + str(tc) + " "
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    n = int(input())
    cmds = input()

    board = solution(h, w, board, n, cmds)
    for i in range(h):
        sb += "".join(board[i]) + "\n"

print(sb)