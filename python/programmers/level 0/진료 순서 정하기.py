def solution(emergency):
    emergency_sort = sorted(emergency, reverse = True)
    dict = {}
    answer = []
    for index in range(len(emergency_sort)):
        dict[emergency_sort[index]] = index + 1
    for e in emergency:
        answer.append(dict[e])
    return answer