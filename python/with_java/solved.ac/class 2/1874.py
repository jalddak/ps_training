from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n):
    queue.appendleft(int(input()))

temp = []
answer = []
for i in range(1, n+1):
    temp.append(i)
    answer.append("+")
    while temp and temp[-1] == queue[-1]:
        queue.pop()
        temp.pop()
        answer.append("-")
    if temp and temp[-1] > queue[-1]:
        print("NO")
        exit()

for a in answer:
    print(a)