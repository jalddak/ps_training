# 에라토스 어쩌구의 체

N = int(input())

checked = [True for _ in range(N + 1)]
checked[0], checked[1] = False, False

sosu = []
for n in range(N+1):
    if not checked[n]:
        continue
    sosu.append(n)

    if n > (int) (N ** 0.5):
        continue
    for m in range(2*n, N+1, n):
        checked[m] = False

from collections import deque

queue = deque([])
temp = 0
result = 0

for n in sosu:
    temp += n
    queue.append(n)

    if temp < N:
        continue
    while temp > N:
        temp -= queue.popleft()
    if temp == N:
        result += 1

print(result)


# 에라토스 시간 줄이는 방법

N = int(input())

checked = [True for _ in range(N + 1)]
checked[0], checked[1] = False, False

sosu = [2]
for n in range(3, N+1, 2):
    if not checked[n]:
        continue
    sosu.append(n)

    if n >= (int) (N ** 0.5):
        continue
    for m in range(n*n, N+1, n):
        checked[m] = False

# 누적합 시간 줄이는 방법(?)

start = 0
end = 0
temp = 0
result = 0

for i in range(len(sosu)):
    temp += sosu[i]
    end = i

    if temp < N:
        continue
    while temp > N:
        temp -= sosu[start]
        start += 1
    if temp == N:
        result += 1

print(result)