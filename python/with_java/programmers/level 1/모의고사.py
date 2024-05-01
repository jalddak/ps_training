def solution(answers):
    cnt = [0, 0, 0]
    for n in range(3):
        if n == 0:
            temp = [1, 2, 3, 4, 5]
            for i in range(len(answers)):
                if answers[i] == temp[i%5]:
                    cnt[n] += 1
            continue
        if n == 1:
            temp = [2, 1, 2, 3, 2, 4, 2, 5]
            for i in range(len(answers)):
                if answers[i] == temp[i%8]:
                    cnt[n] += 1
            continue
        if n == 2:
            temp = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
            for i in range(len(answers)):
                if answers[i] == temp[i%10]:
                    cnt[n] += 1
            continue
    max_cnt = max(cnt)
    answer = []
    for i in range(3):
        if cnt[i] == max_cnt:
            answer.append(i+1)
            
    return answer