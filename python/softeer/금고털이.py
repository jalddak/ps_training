import sys

W, N = map(int, input().split())

js = [list(map(int, input().split())) for _ in range(N)]

js.sort(key=lambda x:-x[1])

result = 0
for weight, cost in js:
    if weight > W:
        result += W * cost
        break
    result += weight * cost
    W -= weight

print(result)