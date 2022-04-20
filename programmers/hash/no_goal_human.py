def solution(participant, completion):
    answer = ''
    hash = {}
    for human in completion:
        if human in hash:
            hash[human] += 1
        else:
            hash[human] = 1
    for human in participant:
        hash[human] = hash.get(human,0) - 1
        if hash.get(human) == -1:
            answer = human
            break
    return answer