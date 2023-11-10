import sys
input = sys.stdin.readline

N, C = map(int, input().split())

houses = [int(input()) for _ in range(N)]
houses.sort()

min_d = 1
max_d = houses[-1]-houses[0]
result = min_d
while (min_d <= max_d):
    mid = (min_d+max_d) // 2
    cnt = 1
    prev_house = houses[0]
    for i in range(1, N):
        if (houses[i] - prev_house >= mid):
            cnt += 1
            prev_house = houses[i]
    
    if cnt >= C:
        result = mid
        min_d = mid + 1
    else:
        max_d = mid - 1

print(result)