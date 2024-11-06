n = int(input())
times = list(map(int, input().split()))

times.sort()
answer = 0
before = 0
for t in times:
    before += t
    answer += before

print(answer)