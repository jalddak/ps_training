def solution(n, results):
    answer = 0
    dic = {}
    for r in results:
        if r[0] not in dic:
            dic[r[0]] = [[r[1]], []]
        else:
            dic[r[0]][0].append(r[1])
        if r[1] not in dic:
            dic[r[1]] = [[], [r[0]]]
        else:
            dic[r[1]][1].append(r[0])
            
    for key in dic:
        queue = dic[key][0][:]
        while len(queue) != 0:
            search = queue.pop()
            for num in dic[search][0]:
                if num not in dic[key][0]:
                    dic[key][0].append(num)
                    queue.append(num)
    
    for key in dic:
        queue = dic[key][1][:]
        while len(queue) != 0:
            search = queue.pop()
            for num in dic[search][1]:
                if num not in dic[key][1]:
                    dic[key][1].append(num)
                    queue.append(num)
                
    for key in dic:
        if len(dic[key][0] + dic[key][1]) == n-1:
            answer += 1
    return answer