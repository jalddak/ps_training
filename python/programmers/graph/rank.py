def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    match = [[] for _ in range(n+1)]
    for result in results:
        win[result[0]].append(result[1])
        lose[result[1]].append(result[0])
    
    for i in range(len(win)):
        for j in win[i]:
            for k in win[j]:
                if k not in win[i]:
                    win[i].append(k)
        for j in lose[i]:
            for k in lose[j]:
                if k not in lose[i]:
                    lose[i].append(k)
    
    for i in range(len(match)):
        match[i] = win[i] + lose[i]

    know = []
    for i in range(len(match)):
        if len(match[i]) == n-1:
            if i not in know:
                know.append(i)
            answer += 1
            
    return answer

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])