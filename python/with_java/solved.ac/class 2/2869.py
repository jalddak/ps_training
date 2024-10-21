a, b, v = map(int, input().split())

h = v - b
r = a - b

answer = h // r + (1 if h % r > 0 else 0)
print(answer)