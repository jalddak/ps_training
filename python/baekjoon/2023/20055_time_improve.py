# 시간복잡도가 개선될 것이라 생각했지만 그렇지 않았다.

from collections import deque

n, k = list(map(int, input().split()))
belt = deque(list(map(int, input().split())))

robots = deque([])
turn = 0
cnt = 0
while True:
    belt.appendleft(belt.pop())
    robots = deque(list(map(lambda x:x+1, list(robots))))
    if len(robots) != 0 and robots[0] == n-1:
        robots.popleft()

    for i in range(len(robots)):
        if belt[robots[i]+1] > 0:
            if i > 0 and robots[i] + 1 == robots[i-1]:
                continue
            belt[robots[i]+1] -= 1
            if belt[robots[i]+1] == 0:
                cnt += 1
            robots[i] += 1
    if len(robots) != 0 and robots[0] == n-1:
        robots.popleft()
    if belt[0] > 0:
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1
        robots.append(0)

    turn += 1

    if cnt >= k:
        print(turn)
        break