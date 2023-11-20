n, k = map(int, input().split())

u = 1
d = 1
for i in range(1, n+1):
    u *= i
for i in range(1, k+1):
    d *= i
for i in range(1, n-k+1):
    d *= i

result = u//d
print(result)