from collections import deque

n, k = list(map(int, input().split()))

belt = deque([])
d = list(map(int, input().split()))
for i in range(2*n):
    belt.append([d[i], 0])

turn = 0
cnt = 0
while True:
    belt.appendleft(belt.pop())
    if belt[n-1][1] == 1:
        belt[n-1][1] = 0

    for i in range(n-1, -1, -1):
        if belt[i][1] == 1 and belt[i+1][0] > 0 and belt[i+1][1] == 0:
            belt[i+1][0] -= 1
            if belt[i+1][0] == 0:
                cnt += 1
            belt[i+1][1] = 1
            belt[i][1] = 0
    if belt[n-1][1] == 1:
        belt[n-1][1] = 0
    
    if belt[0][0] > 0:
        belt[0][0] -= 1
        if belt[0][0] == 0:
            cnt += 1
        belt[0][1] = 1
    turn += 1

    if cnt >= k:
        print(turn)
        break