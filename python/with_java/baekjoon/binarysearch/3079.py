import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = []
for _ in range(n):
    t.append(int(input()))

cover = m // n + (1 if m % n > 0 else 0)
minT = min(t)
maxT = max(t)

s = minT * cover - 1
e = maxT * cover + 1

def bs(s, e):
    while s + 1 < e:
        mid = (s + e) // 2

        temp = 0
        for time in t:
            temp += mid // time
        
        if temp < m:
            s = mid
        else:
            e = mid
    return e

print(bs(s, e))