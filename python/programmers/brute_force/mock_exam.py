answers = [1,2,1,1,2]

def solution(answers):
    answer = []
    s1 = 0
    s2 = 0
    s3 = 0
    i = 0
    while i < len(answers):
        if (i+1) % 5 == answers[i] % 5:
            s1 += 1
            
        if (i+1) % 2 == 1 and answers[i] == 2:
            s2 += 1
        elif (i+1) % 8 == 2 and answers[i] == 1:
            s2 += 1
        elif (i+1) % 8 == 4 and answers[i] == 3:
            s2 += 1
        elif (i+1) % 8 == 6 and answers[i] == 4:
            s2 += 1
        elif (i+1) % 8 == 0 and answers[i] == 5:
            s2 += 1
            
        if (i+1) % 10 == 1 or (i+1) % 10 == 2:
            if answers[i] == 3:
                s3 += 1
        elif (i+1) % 10 == 3 or (i+1) % 10 == 4:
            if answers[i] == 1:
                s3 += 1
        elif (i+1) % 10 == 5 or (i+1) % 10 == 6:
            if answers[i] == 2:
                s3 += 1
        elif (i+1) % 10 == 7 or (i+1) % 10 == 8: 
            if answers[i] == 4:
                s3 += 1
        elif (i+1) % 10 == 9 or (i+1) % 10 == 0:
            if answers[i] == 5:
                s3 += 1
        i += 1
    
    if s1 > s2:
        if s1 > s3:
            answer.append(1)
        elif s1 == s3:
            answer.append(1)
            answer.append(3)
        elif s1 < s3:
            answer.append(3)
    elif s1 == s2:
        if s1 > s3:
            answer.append(1)
            answer.append(2)
        elif s1 == s3:
            answer.append(1)
            answer.append(2)
            answer.append(3)
        elif s1 < s3:
            answer.append(3)
    elif s1 < s2:
        if s2 > s3:
            answer.append(2)
        elif s2 == s3:
            answer.append(2)
            answer.append(3)
        elif s2 < s3:
            answer.append(3)
    
    return answer

solution(answers)