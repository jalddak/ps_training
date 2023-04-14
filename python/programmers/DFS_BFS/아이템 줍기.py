def solution(rectangle, characterX, characterY, itemX, itemY):
    back = [[' ' for _ in range(102)] for _ in range(102)]
    for r in rectangle:
        for i in range(2*r[1],2*r[3]+1):
            for j in range(2*r[0],2*r[2]+1):
                if i == 2*r[1] or i == 2*r[3] or j == 2*r[0] or j == 2*r[2]:
                    if back[i][j] == ' ':
                        back[i][j] = '2'
                else:
                    back[i][j] = '1'
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cX = characterX * 2
    cY = characterY * 2
    locations = []
    for i in range(4):
        nextY = cY + dy[i]
        nextX = cX + dx[i]
        if back[nextY][nextX] == '2':
            locations.append([nextY,nextX,i])
    cnt = 1
    while True:
        cnt += 1
        for i in range(len(locations)):
            cY = locations[i][0]
            cX = locations[i][1]
            before = locations[i][2] + 2
            if before > 4:
                before -= 4
            for j in range(4):
                nextY = cY + dy[j]
                nextX = cX + dx[j]
                if nextY == 2*itemY and nextX == 2*itemX:
                    return cnt / 2
                if back[nextY][nextX] == '2' and before != j:
                    locations[i] = [nextY,nextX,j]