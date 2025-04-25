import sys
input = sys.stdin.readline

import heapq

t = int(input())
answer = []
for _ in range(t):
    k = int(input())
    min_h = []
    max_h = []
    d = dict()

    for _ in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
            heapq.heappush(min_h, n)
            heapq.heappush(max_h, (-n, n))
        elif cmd == 'D':
            if n == -1:
                while min_h:
                    delN = heapq.heappop(min_h)
                    if delN in d and d[delN] > 0:
                        d[delN] -= 1
                        break
            elif n == 1:
                while max_h:
                    delN = heapq.heappop(max_h)[1]
                    if delN in d and d[delN] > 0:
                        d[delN] -= 1
                        break
                    
    maxN, minN = 0, 0
    while max_h:
        n = max_h[0][1]
        if n in d and d[n] > 0:
            maxN = n
            break
        heapq.heappop(max_h)
    while min_h:
        n = min_h[0]
        if n in d and d[n] > 0:
            minN = n
            break
        heapq.heappop(min_h)
        
    
    if max_h:
        answer.append(str(maxN) + " " + str(minN))
    else:
        answer.append("EMPTY")

for a in answer:
    print(a)