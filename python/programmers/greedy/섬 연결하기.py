def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    connects = []
    fees = []
    for c in costs:
        check = 0
        first_i = -1
        second_i = -1
        flag = 0
        for i in range(len(connects)):
            if c[0] in connects[i] and c[1] in connects[i]:
                flag = 1
                break
            elif c[0] in connects[i]:
                first_i = i
                check += 1
            elif c[1] in connects[i]:
                second_i = i
                check += 1
        if flag == 1:
            continue
            
        if check == 0:
            connects.append([c[0], c[1]])
            fees.append(c[2])
        elif check == 1:
            if first_i != -1:
                connects[first_i].append(c[1])
                fees[first_i] += c[2]
            elif second_i != -1:
                connects[second_i].append(c[0])
                fees[second_i] += c[2]
        elif check == 2:
            if first_i < second_i:
                connects[first_i] += connects[second_i]
                del connects[second_i]
                fees[first_i] += c[2] + fees[second_i]
                del fees[second_i]
            elif first_i > second_i:
                connects[second_i] += connects[first_i]
                del connects[first_i]
                fees[second_i] += c[2] + fees[first_i]
                del fees[first_i]
                
        if len(connects[0]) == n:
            break
        
    answer = fees[0]
                
    return answer