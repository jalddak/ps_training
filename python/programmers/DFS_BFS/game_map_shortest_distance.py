from collections import deque

def solution(maps):
    # 북 동 남 서
    x_move = [0, 1, 0, -1]
    y_move = [-1, 0, 1, 0]
    y_len = len(maps)
    x_len = len(maps[0])
    queue = deque([])
    queue.append([0,0,1])
    while len(queue) != 0:
        y_loca, x_loca, result = queue.popleft()
        result += 1
        maps[y_loca][x_loca] = 0
        for i in range(4):
            y_after = y_loca + y_move[i]
            x_after = x_loca + x_move[i]
            if y_after >= 0 and y_after < y_len\
            and x_after >= 0 and x_after < x_len:
                if y_after == y_len-1 and x_after == x_len-1:
                    return result
                if maps[y_after][x_after] != 0:
                    maps[y_after][x_after] = 0
                    queue.append([y_after, x_after, result])
    return -1