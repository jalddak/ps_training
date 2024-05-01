def check(info):
    for key in info:
        if info[key] != 0:
            return False
    return True

def solution(want, number, discount):
    info = {}
    for i in range(len(want)):
        info[want[i]] = number[i]
    for i in range(9):
        if discount[i] in info:
            info[discount[i]] -= 1
    answer = 0
    for i in range(9, len(discount)):
        if discount[i] in info:
            info[discount[i]] -= 1
        if check(info):
            answer += 1
        if discount[i-9] in info:
            info[discount[i-9]] += 1
    return answer