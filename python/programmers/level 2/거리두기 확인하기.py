def solution(places):
    answer = []
    dy = [-1, 0, 1, 2]
    dx = [1, 2, 1, 0]
    for place in places:
        check = True
        for y in range(5):
            for x in range(5):
                if place[y][x] != 'P':
                    continue
                if 0<=y+1<5 and place[y+1][x] == 'P':
                    check = False
                    break
                if 0<=x+1<5 and place[y][x+1] == 'P':
                    check = False
                    break
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0<=ny<5 and 0<=nx<5 and place[ny][nx] == 'P':
                        if d == 0 and (place[y-1][x] == 'O' or place[y][x+1] == 'O'):
                            check = False
                        if d == 1 and place[y][x+1] == 'O':
                            check = False
                        if d == 2 and (place[y+1][x] == 'O' or place[y][x+1] == 'O'):
                            check = False
                        if d == 3 and place[y+1][x] == 'O':
                            check = False
                    if not check:
                        break
                if not check:
                    break
            if not check:
                break
        if check:
            answer.append(1)
        else:
            answer.append(0)
                
                
    return answer