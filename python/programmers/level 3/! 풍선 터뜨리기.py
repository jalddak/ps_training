# 아이디어 확인
def solution(a):
    answer = 1
    min_index = a.index(min(a))
    left_min = 0
    for i in range(min_index):
        if i != 0 and left_min < a[i]:
            continue
        answer += 1
        left_min = a[i]
    right_min = 0
    for i in range(len(a)-1, min_index, -1):
        if i != len(a)-1 and right_min < a[i]:
            continue
        answer += 1
        right_min = a[i]
    
    return answer