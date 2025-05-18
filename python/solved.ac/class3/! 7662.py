import heapq
import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    k = int(input())
    min_h = []
    max_h = []
    visited = [False for _ in range(k)]
    for i in range(k):
        command = input().split()
        if command[0] == 'I':
            num = int(command[1])
            heapq.heappush(min_h, (num, i))
            heapq.heappush(max_h, (-num, i))
        elif command[0] == 'D':
            if command[1] == "-1" and len(min_h) != 0:
                index = heapq.heappop(min_h)[1]
                visited[index] = True
            elif command[1] == "1" and len(max_h) != 0:
                index = heapq.heappop(max_h)[1]
                visited[index] = True
        
        while len(min_h) != 0 and visited[min_h[0][1]]:
            heapq.heappop(min_h)
        while len(max_h) != 0 and visited[max_h[0][1]]:
            heapq.heappop(max_h)

    if len(min_h) == 0:
        result.append('EMPTY')
    else:
        r = str(-heapq.heappop(max_h)[0]) + ' ' + str(heapq.heappop(min_h)[0])

for r in result:
    print(r)



# 시간초과

import heapq
import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    k = int(input())
    Q = []
    flag = -1
    for _ in range(k):
        command = input().split()
        if command[0] == 'I':
            num = int(command[1])
            heapq.heappush(Q, (num * (-flag), num))
        elif command[0] == 'D' and len(Q) != 0:
            if flag != int(command[1]):
                Q = list(map(lambda x:(-x[0], x[1]), Q))
                flag = -flag
                heapq.heapify(Q)
                heapq.heappop(Q)
            else:
                heapq.heappop(Q)

    if len(Q) == 0:
        result.append('EMPTY')
    else:
        l = list(map(lambda x:x[1], Q))
        r = str(max(l)) + ' ' + str(min(l))
        result.append(r)

for r in result:
    print(r)