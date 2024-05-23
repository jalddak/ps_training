def solution(babbling):
    can = {"aya", "ye", "woo", "ma"}
    answer = 0
    for word in babbling:
        before = ''
        current = ''
        flag = True
        for c in word:
            current += c
            if current in can and before != current:
                before = current
                current = ''
            if len(current) > 3:
                break
        if current != '':
            flag = False
        if flag:
            answer += 1
    return answer