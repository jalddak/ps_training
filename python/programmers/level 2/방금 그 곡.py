def code_select(code):
    length = len(code)
    result = []
    i = 0
    while i < length:
        c = code[i]
        if i < length-1 and code[i+1] == '#':
            c += '#'
            i += 1
        i += 1
        result.append(c)
    return result

def time_calc(time):
    time = time.split(':')
    time = int(time[0]) * 60 + int(time[1])
    return time

def solution(m, musicinfos):
    candidate = []
    m = code_select(m)
    for mi in musicinfos:
        start, end, title, code = mi.split(",")
        start, end = time_calc(start), time_calc(end)
        length = end - start
        if length < len(m):
            continue
        code = code_select(code)
        realcode = code * (length // len(code)) + code[:length%len(code)]
        for i in range(length - len(m)+1):
            subcode = realcode[i:i+len(m)]
            if m == subcode:
                candidate.append((length, title))
    
    if not candidate:
        return '(None)'
    candidate.sort(key=lambda x:-x[0])
    return candidate[0][1]