routes = [[0,12],[1,12],[2,12],[3,12],[5,6],[6,12],[10,12]]

def solution(routes):
    answer = 0
    routes.sort(key = lambda x: (x[0], x[1]))
    i = 0
    while i < len(routes):
        j = i + 1
        short = routes[i][1]
        while j < len(routes):
            if routes[j][0] <= short:
                if short > routes[j][1]:
                    short = routes[j][1]
                j += 1
            else:
                i = j
                break
        if j == len(routes):
            i = j
        if i != j:
            i += 1 
        answer += 1
    
    print(answer)

    return answer

solution(routes)