def solution(lottos, win_nums):
    check = 0
    per = 0
    for num in lottos:
        if num == 0:
            per += 1
        if num in win_nums:
            check += 1
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer = [rank[check+per], rank[check]]
    return answer