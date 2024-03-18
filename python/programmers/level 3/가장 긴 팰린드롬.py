from collections import deque

def solution(s):
    answer = 0
    
    n = len(s)
    queue = deque()
    for i in range(n):
        queue.append((i, i))
    for i in range(n-1):
        if s[i] == s[i+1]:
            queue.append((i, i+1))
    
    while queue:
        l, r = queue.popleft()
        length = r-l+1
        answer = max(length, answer)
        if l-1 >= 0 and r+1 < n and s[l-1] == s[r+1]:
            queue.append((l-1, r+1))

    return answer