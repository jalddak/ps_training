import sys

input = sys.stdin.readline

def gcd(m, n):
    while n != 0:
        nn = m % n
        m = n
        n = nn
    return m

def lcm(m, n):
    return m * n / gcd(m, n)

results = []

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    answer, a, b = x, x, x if m <= n else x % n
    b = n if b == 0 else b
    flag = False
    end = lcm(m, n)
    while answer <= end:
        if a == x and b == y:
            flag = True
            break
        b = b + m if b + m <= n else (b + m) % n
        b = n if b == 0 else b
        answer += m
    if not flag:
        answer = -1
    results.append(answer)

for r in results:
    print(r)