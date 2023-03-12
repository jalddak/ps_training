def solution(n, wires):
    answer = n
    w_d = {}
    for i in range(len(wires)):
        w = tuple(wires[i])
        w_d[w] = [[w[0]], [w[1]]]
        
        j = 0
        while j < len(wires):
            if i == j:
                j += 1
                continue
            for k in range(len(w_d[w])):
                if len(set(w_d[w][k]) & set(wires[j])) == 1:
                    w_d[w][k] = list(set(w_d[w][k]) | set(wires[j]))
                    j = -1
                    break
            j += 1
    
    for key in w_d:
        left = len(w_d[key][0])
        right = len(w_d[key][1])
        dif = abs(left - right)
        if answer > dif:
            answer = dif
        
    return answer

#       위에가 정답 아래는 고민한거 근데 예전에 풀었을때보다 코드는 간결하지만 실행속도는 엄청떨어진다. 하루종일 이것만풀었다. 큰일났다.

----------------------------------------


def solution(n, wires):
    answer = -1
    w_d = {}
    wires = sorted(wires, key=lambda x:(x[0], x[1]))
    for w in wires:
        if w[0] not in w_d:
            w_d[w[0]] = [[w[1]]]
        else:
            w_d[w[0]].append([w[1]])
        if w[1] not in w_d:
            w_d[w[1]] = [[w[0]]]
        else:
            w_d[w[1]].append([w[0]])
    
    for key in w_d:
        for array in w_d[key]:
            for w in wires:
                if w[0] in array and key != w[1]:
                    array.append(w[1])
                elif w[1] in array and key != w[0]:
                    array.append(w[0])
    
    wires = sorted(wires, key=lambda x:(-x[1], -x[0]))
    for key in w_d:
        for array in w_d[key]:
            for w in wires:
                if w[0] in array and key != w[1]:
                    array.append(w[1])
                elif w[1] in array and key != w[0]:
                    array.append(w[0])
    candidates = []
    candidate = []
    for key in w_d:
        candidate.append(1)
        for i in range(len(w_d[key])):
            w_d[key][i] = list(set(w_d[key][i]))
            candidate.append(len(w_d[key][i]))
        candidates.append(candidate)
        candidate = []
    
    answer = len(wires)
    for c in candidates:
        max_num = max(c)
        another = sum(c) - max_num
        min_dif = abs(another - max_num)
        
        answer = min_dif if answer > min_dif else answer
    return answer



--------------------------------


def solution(n, wires):
    answer = -1
    w_d = {}
    wires = sorted(wires, key=lambda x:(x[0], x[1]))
    for w in wires:
        if w[0] not in w_d and w[1] not in w_d:
            w_d[w[0]] = [[w[1]]]
        elif w[0] in w_d:
            w_d[w[0]].append([w[1]])
        elif w[1] in w_d:
            w_d[w[1]].append([w[0]])
            w_d[w[0]] = []
        if w[1] not in w_d:
            w_d[w[1]] = []
            
        for key in w_d:
            for array in w_d[key]:
                if w[0] in array and key != w[1]:
                    array.append(w[1])
                elif w[1] in array and key != w[0]:
                    array.append(w[0])
    
    num = n
    answer = n
    for key in w_d:
        for array in w_d[key]:
            team1 = len(array)
            team2 = num - len(array)
            dif = abs(team1 - team2)
            answer = dif if answer > dif else answer
    return answer