def solution(dirs):
    L = [-1, 0]
    R = [1, 0]
    U = [0, 1]
    D = [0, -1]
    now_loca = (0, 0)
    passed_road = {}
    answer = 0
    
    for direction in dirs:
        if direction == 'L' and now_loca[0] != -5:
            next_loca = (now_loca[0] - 1, now_loca[1])
        elif direction == 'R' and now_loca[0] != 5:
            next_loca = (now_loca[0] + 1, now_loca[1])
        elif direction == 'U' and now_loca[1] != -5:
            next_loca = (now_loca[0], now_loca[1] - 1)
        elif direction == 'D' and now_loca[1] != 5:
            next_loca = (now_loca[0], now_loca[1] + 1)
        else:
            continue
        
        if now_loca not in passed_road:
            passed_road[now_loca] = [next_loca]
            answer += 1
        elif next_loca not in passed_road[now_loca]:
            passed_road[now_loca].append(next_loca)
            answer += 1
        if next_loca not in passed_road:
            passed_road[next_loca] = [now_loca]
        elif now_loca not in passed_road[next_loca]:
            passed_road[next_loca].append(now_loca)
        
        now_loca = next_loca
        
    return answer