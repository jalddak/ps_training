def solution(lines):
    answer = 0
    lines.sort(key=lambda x:x[0])
    겹 = []
    if lines[0][1] > lines[1][0]:
        겹.append([lines[1][0], min(lines[0][1], lines[1][1])])
    if lines[0][1] > lines[2][0]:
        겹.append([lines[2][0], min(lines[0][1], lines[2][1])])
    if lines[1][1] > lines[2][0]:
        겹.append([lines[2][0], min(lines[1][1], lines[2][1])])
        
    겹.sort(key=lambda x:(x[0], x[1]))
    print(겹)
    if len(겹) == 1:
        answer += 겹[0][1] - 겹[0][0]
    if len(겹) == 2:
        if 겹[0][1] < 겹[1][0]:
            answer += 겹[0][1] - 겹[0][0] + 겹[1][1] - 겹[1][0]
        else:
            중복 = [겹[0][0], max(겹[0][1], 겹[1][1])]
            answer += 중복[1] - 중복[0]
    if len(겹) == 3:
        if 겹[0][1] < 겹[1][0]:
            answer += 겹[0][1] - 겹[0][0]
            if 겹[1][1] < 겹[2][0]:
                answer += 겹[1][1] - 겹[1][0] + 겹[2][1] - 겹[2][0]
            else:
                answer += max(겹[1][1], 겹[2][1])- 겹[1][0]
        else:
            중복 = [겹[0][0], max(겹[0][1], 겹[1][1])]
            answer += 중복[1] - 중복[0]
            if 중복[1] < 겹[2][0]:
                answer += 겹[2][1] - 겹[2][0]
            else:
                answer += max(중복[1], 겹[2][1])- 중복[1]

        
            
        
    return answer