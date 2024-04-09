def check(board, x, y, a):
    if a == 0:
        if y == 0 \
        or 1 in board[y][x] \
        or (x > 0 and 1 in board[y][x-1]) \
        or (y > 0 and 0 in board[y-1][x]):
            return True
    elif a == 1:
        if 0 in board[y-1][x] \
        or 0 in board[y-1][x+1] \
        or (x > 0 and 1 in board[y][x-1] and 1 in board[y][x+1]):
            return True
    return False
    

def solution(n, build_frame):
    board = [[[] for _ in range(n+1)] for _ in range(n+1)]
    for x, y, a, b in build_frame:
        if b == 1 and check(board, x, y, a):
            board[y][x].append(a)
            continue
        elif b == 0 and a == 0:
            board[y][x].remove(a)
            if 0 in board[y+1][x] and not check(board, x, y+1, 0):
                board[y][x].append(a)
                continue
            if 1 in board[y+1][x] and not check(board, x, y+1, 1):
                board[y][x].append(a)
                continue
            if x > 0 and 1 in board[y+1][x-1] and not check(board, x-1, y+1, 1):
                board[y][x].append(a)
                continue
        elif b == 0 and a == 1:
            board[y][x].remove(a)
            if 0 in board[y][x] and not check(board, x, y, 0):
                board[y][x].append(a)
                continue
            if 0 in board[y][x+1] and not check(board, x+1, y, 0):
                board[y][x].append(a)
                continue
            if 1 in board[y][x+1] and not check(board, x+1, y, 1):
                board[y][x].append(a)
                continue
            if x > 0 and 1 in board[y][x-1] and not check(board, x-1, y, 1):
                board[y][x].append(a)
                continue
    
    answer = []
    for x in range(n+1):
        for y in range(n+1):
            if board[y][x]:
                board[y][x].sort()
                for a in board[y][x]:
                    answer.append([x, y, a])
                    
    return answer