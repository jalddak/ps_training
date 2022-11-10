def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        before_len = len(s)
        s = s.replace('0', '')
        after_len = len(s)
        answer[1] += before_len - after_len
        s = bin(after_len)[2:]
    
    return answer