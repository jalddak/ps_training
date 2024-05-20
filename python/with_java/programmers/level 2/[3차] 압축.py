def solution(msg):
    start = ord('A')
    d = {}
    num = 26
    for i in range(num):
        d[chr(start + i)] = i+1
    num += 1
    answer = []
    index = 0
    while index < len(msg):
        w = msg[index]
        temp = d[w]
        while index + 1 < len(msg):
            if w + msg[index+1] in d:
                w = w + msg[index+1]
                temp = d[w]
                index += 1
                continue
            break
        if index + 1 < len(msg):
            d[w + msg[index+1]] = num
            num += 1
        answer.append(temp)
        index += 1
        
    return answer