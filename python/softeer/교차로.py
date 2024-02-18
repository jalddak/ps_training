import sys
input = sys.stdin.readline

from collections import deque
import heapq

N = int(input())

tws = deque([])
for _ in range(N):
    t, w = input().split()
    t = int(t)
    tws.append((t, w))

abcd_queue = [deque() for _ in range(4)]
answer = [-1 for _ in range(N)]

def push_i(t, w, i):
    a, b, c, d = abcd_queue
    if w == 'A':
        a.append((t, i))
    if w == 'B':
        b.append((t, i))
    if w == 'C':
        c.append((t, i))
    if w == 'D':
        d.append((t, i))
        
i = 0
while i < N:
    t, w = tws[i]
    push_i(t, w, i)
    i += 1
    while i < N and t == tws[i][0]:
        t, w = tws[i]
        push_i(t, w, i)
        i += 1
    while abcd_queue[0] or abcd_queue[1] or abcd_queue[2] or abcd_queue[3]:
        a,b,c,d = abcd_queue
        check = [False] * 4
        if a and not d:
            check[0] = True
        if b and not a:
            check[1] = True
        if c and not b:
            check[2] = True
        if d and not c:
            check[3] = True
        if set(check) == {False}:
            for num in answer:
                print(num)
            exit()

        popt = 0
        for j in range(4):
            if check[j]:
                popt, popi = abcd_queue[j].popleft()
                answer[popi] = popt
            abcd_queue[j] = deque(map(lambda x:(x[0]+1, x[1]), abcd_queue[j]))
            
        while i < N and popt+1 == tws[i][0]:
            t, w = tws[i]
            push_i(t, w, i)
            i += 1
        
for num in answer:
    print(num) 