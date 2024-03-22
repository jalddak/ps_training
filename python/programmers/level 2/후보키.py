from itertools import combinations

def solution(relation):
    answer = 0
    results = []
    r, c = len(relation), len(relation[0])
    cols = [i for i in range(c)]
    for i in range(1, c+1):
        check_list = list(combinations(cols, i))
        for cl in check_list:
            candidate = set()
            for row in relation:
                temp = []
                for n in cl:
                    temp.append(row[n])
                temp = tuple(temp)
                candidate.add(temp)
            if len(candidate) == r:
                cl = set(cl)
                check = True
                for result in results:
                    if result & cl == result:
                        check = False
                        break
                if check:
                    results.append(cl)
    
    answer = len(results)
    
    return answer