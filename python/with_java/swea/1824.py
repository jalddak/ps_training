dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

direction = {"^":0, ">":1, "v":2, "<":3}

tcCnt = int(input())

answer = []

def nextCheck(r, c, y, x, d, stack, visited, memory):
    ny = y + dy[d]
    nx = x + dx[d]
    if ny >= r:
        ny = 0
    if ny < 0:
        ny = r - 1
    if nx >= c:
        nx = 0
    if nx < 0:
        nx = c - 1
    
    if visited[ny][nx][d][memory]:
        return
    
    visited[ny][nx][d][memory] = True
    stack.append((ny, nx, d))
    


for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]
    memory = 0
    visited = [[[[False for _ in range(16)] for _ in range(4)] for _ in range(c)] for _ in range(r)]

    stack = [(0, 0, 1)]
    visited[0][0][2][memory] = True

    result = "NO"
    while stack:
        y, x, d = stack.pop()
        if board[y][x] in set(direction.keys()):
            d = direction[board[y][x]]
            nextCheck(r, c, y, x, d, stack, visited, memory)
        elif board[y][x] == "_":
            if memory == 0:
                d = 1
            else:
                d = 3
            nextCheck(r, c, y, x, d, stack, visited, memory)
        elif board[y][x] == "|":
            if memory == 0:
                d = 2
            else:
                d = 0
            nextCheck(r, c, y, x, d, stack, visited, memory)
        elif board[y][x] == "?":
            for d in range(4):
                nextCheck(r, c, y, x, d, stack, visited, memory)
        elif board[y][x] == ".":
            nextCheck(r, c, y, x, d, stack, visited, memory)
        elif board[y][x] == "@":
            result = "YES"
            break
        elif board[y][x] in set(map(str, [i for i in range(10)])):
            memory = int(board[y][x])
            nextCheck(r, c, y, x, d, stack, visited, memory)
        elif board[y][x] == "+":
            memory += 1
            if memory == 16:
                memory = 0
            nextCheck(r, c, y, x, d, stack, visited, memory)
        elif board[y][x] == "-":
            memory -= 1
            if memory == -1:
                memory = 15
            nextCheck(r, c, y, x, d, stack, visited, memory)
    
    sb += result
    answer.append(sb)

for a in answer:
    print(a)