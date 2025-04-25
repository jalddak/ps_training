import sys
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key = lambda x:(x[1], x[0]))

before = 0
answer = 0
for t in times:
    s, e = t
    if before <= s:
        before = e
        answer += 1

print(answer)
