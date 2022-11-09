def solution(lottos, win_nums):
    answer = [6, 6]
    check = 0
    zero_cnt = lottos.count(0)
    for num in lottos:
        if num in win_nums:
            check += 1
    
    result = [check, check+zero_cnt]
    
    for n in range(1, 7):
        if result[0] == n:
            answer[1] = 7 - n
        if result[1] == n:
            answer[0] = 7 - n
    return answer