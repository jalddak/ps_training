def solution(array, commands):
    answer = []
    for c in commands:
        select = array[c[0]-1:c[1]]
        select.sort()
        answer.append(select[c[2]-1])
    return answer