def solution(s):
    temp = s[2:-2].split("},{")
    lists = []
    answer = []
    for t in temp:
        lists.append(list(map(int, t.split(","))))
    lists.sort(key=lambda x:len(x))
    for l in lists:
        temp = answer[:];
        for n in l:
            if n in temp:
                temp.remove(n)
            else:
                answer.append(n)
                
    return answer