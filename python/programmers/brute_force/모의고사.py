def solution(answers):
    answer = []
    human = [0, 0, 0]
    for i in range(len(answers)):
        i += 1
        o_c = i % 5
        if o_c == 0:
            o_c = 5
            
        t_c = i % 8
        if t_c % 2 == 1:
            t_c = 2
        elif t_c // 2 == 1:
            t_c = 1
        elif t_c // 2 == 2:
            t_c = 3
        elif t_c // 2 == 3:
            t_c = 4
        elif t_c // 2 == 0:
            t_c = 5
            
        th_c = i % 10
        if th_c == 1 or th_c == 2:
            th_c = 3
        elif th_c == 3 or th_c == 4:
            th_c = 1
        elif th_c == 5 or th_c == 6:
            th_c = 2
        elif th_c == 7 or th_c == 8:
            th_c = 4
        else:
            th_c = 5
            
        i -= 1
        
        if answers[i] == o_c:
            human[0] += 1
        if answers[i] == t_c:
            human[1] += 1
        if answers[i] == th_c:
            human[2] += 1
    
    max_score = max(human)
    for i in range(len(human)):
        if human[i] == max_score:
            answer.append(i+1)
    
    return answer