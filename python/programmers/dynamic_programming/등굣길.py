def solution(m, n, puddles):
    dx = [1, 0]
    dy = [0, 1]
    location = [[0 for col in range(m+1)] for row in range(n+1)]
    answer = 0
    route = [[1,1]]
    location[1][1] = 1
    while location[n][m] == 0:
        update = []
        for r in route:
            for i in range(len(dx)):
                x = dx[i] + r[0]
                y = dy[i] + r[1]
                if [x,y] not in puddles and x <= m and y <= n:
                    location[y][x] += location[r[1]][r[0]]
                    location[y][x] = location[y][x] % 1000000007
                    if [x,y] not in update:
                        update.append([x,y])
        route = update
        if len(route) == 0:
            break
    
    answer = location[n][m]
    
    return answer