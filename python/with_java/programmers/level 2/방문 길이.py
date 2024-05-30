def solution(dirs):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    dir_info = {'U':0, 'R':1, 'D':2, 'L':3}
    visited = {}
    y, x = 0, 0
    answer = 0
    
    for direction in dirs:
        d = dir_info[direction]
        ny = y + dy[d]
        nx = x + dx[d]
        rd = d-2 if d-2 >= 0 else d+2
        if not (-5<=ny<=5 and -5<=nx<=5):
            continue
        visited[(y, x)] = visited.get((y, x), [False for _ in range(4)]);
        if not visited[(y, x)][d]:
            visited[(y, x)][d] = True
            visited[(ny, nx)] = visited.get((ny, nx), [False for _ in range(4)])
            visited[(ny, nx)][rd] = True
            answer += 1
        y, x = ny, nx
        
    return answer