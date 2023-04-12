from collections import deque

def solution(maps):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    m = len(maps) # y좌표 끝
    n = len(maps[0]) # x좌표 끝
    
    maps[0][0] = 0
    candidates = deque([[0, 0, 1]]) # 맵, y좌표, x좌표, 밟은칸수
    
    while len(candidates) != 0:
        y_l, x_l, cnt = candidates.popleft()
        cnt += 1
        for i in range(4):
            y_m = y_l + dy[i]
            x_m = x_l + dx[i]
            if y_m < m and y_m >= 0 and x_m < n and x_m >= 0:
                if y_m == m-1 and x_m == n-1:
                    return cnt
                if maps[y_m][x_m] != 0:
                    maps[y_m][x_m] = 0
                    candidates.append([y_m, x_m, cnt])
                
    return -1