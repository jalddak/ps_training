# 코드는 안봤지만, 아이디어 자체가 생각나지 않아서 푸는 방법 확인한 문제임.

from collections import deque

n = int(input())
length = len(bin(n)[2:])

cnt = int(input())
q = deque(map(int, input().split()))

INF = 10 ** 2
arr = [INF for _ in range(n + 1)]

for num in q:
    arr[num] = 0

answer = 0
def xor(num):
    global n, length, answer
    for i in range(length):
        next = num ^ (1 << i)
        if next <= n and arr[next] > arr[num] + 1:
            arr[next] = arr[num] + 1
            q.append(next)
            answer = arr[next]
            
while q:
    num = q.popleft()
    xor(num)

print(answer)