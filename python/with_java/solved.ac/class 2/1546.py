cnt = int(input())
scores = list(map(int, input().split()))

mx = max(scores)

answer = 0
for s in scores:
    answer += s/mx * 100

answer /= cnt
print(answer)