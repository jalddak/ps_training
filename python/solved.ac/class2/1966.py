from collections import deque
import sys
input = sys.stdin.readline

cnt = int(input())

for _ in range(cnt):
    N, M = map(int, input().split())
    l = deque(list(map(int, input().split())))
    i = 0
    while len(l) != 0:
        if l[0] == max(l):
            i += 1
            l.popleft()
            if M == 0:
                break
        elif l[0] != max(l):
            l.append(l.popleft())
            if M == 0:
                M = len(l)
        M -= 1
    print(i)
            
    
