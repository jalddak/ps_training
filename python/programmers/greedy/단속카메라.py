def solution(routes):
    answer = 0
    routes.sort(key = lambda x:(x[0], x[1]))
    ables = []
    for r in routes:
        check = 0
        for a in ables:
            if r[0] >= a[0] and r[0] <= a[1]:
                check = 1
                a[0] = r[0]
                if r[1] < a[1]:
                    a[1] = r[1] 
        if check == 0:
            ables.append(r)
    answer = len(ables)
    return answer