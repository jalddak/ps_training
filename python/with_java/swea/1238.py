from collections import deque

tcCnt = 10

answer = []

for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    length, start = map(int, input().split())

    info = {}
    ip = list(map(int, input().split()))
    for i in range(0, length, 2):
        f = ip[i]
        t = ip[i+1]
        if f not in info:
            info[f] = [t]
        else:
            info[f].append(t)
    
    q = deque([])
    visited = set()

    q.append((start, 0))
    visited.add(start)

    candidates = []
    maxW = -1
    while q:
        x, w = q.popleft()
        if maxW < w:
            maxW = w
            candidates = []
        candidates.append(x)
        if x not in info:
            continue
        for nx in info[x]:
            if nx in visited:
                continue
            q.append((nx , w + 1))
            visited.add(nx)
    
    result = max(candidates)

    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)