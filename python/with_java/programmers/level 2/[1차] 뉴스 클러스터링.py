def make_list(string):
    result = []
    for i in range(len(string)-1):
        if string[i].islower() and string[i+1].islower():
            result.append(string[i] + string[i+1])
    return result

def make_dict(l):
    d = {}
    for w in l:
        d[w] = d.get(w, 0) + 1
    return d
    

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    l1 = make_list(str1)
    l2 = make_list(str2)
    d1 = make_dict(l1)
    d2 = make_dict(l2)
    inter = 0
    union = 0
    for w in d1:
        if w in d2:
            temp = min(d1[w], d2[w])
            inter += temp
            union += temp
            d1[w] -= temp
            d2[w] -= temp
        union += d1[w]
    for w in d2:
        union += d2[w]
    
    if union == 0:
        return 65536
    answer = int((inter / union) * 65536)
    return answer