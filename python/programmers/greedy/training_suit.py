n, lost, reserve = (
        30,
        [1, 2, 7, 9, 10, 11, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27], # 16개
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 22, 23, 24, 25, 26, 27, 28], # 25개
    )

def solution(n, lost, reserve):
    answer = 0
    index = 0
    lost.sort()
    while index < len(lost):
        if lost[index] in reserve:
            reserve.remove(lost[index])
            lost.remove(lost[index])
            index -= 1
        index += 1
    for lost_student in lost:
        if lost_student-1 in reserve:
            reserve.remove(lost_student-1)
        elif lost_student+1 in reserve:
            reserve.remove(lost_student+1)
        else:
            n -= 1
    answer = n
    return answer

solution(n, lost, reserve)