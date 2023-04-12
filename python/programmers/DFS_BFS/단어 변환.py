from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([[begin, words, 0]])
    while len(queue) != 0:
        now, words, cnt = queue.popleft()
        cnt += 1
        for w in words:
            copy_w = words[:]
            check = 0
            for i in range(len(now)):
                if w[i] != now[i]:
                    check += 1
            if check == 1:
                if w == target:
                    return cnt
                copy_w.remove(w)
                queue.append([w, copy_w, cnt])
    answer = 0
    return answer