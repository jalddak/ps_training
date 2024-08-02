N = int(input())
tang = list(map(int, input().split()))
l = [0 for _ in range(10)]

answer = 0
left, right = 0, 0
kind = 0

for i in range(N):
    l[tang[i]] += 1
    if l[tang[i]] == 1:
        kind += 1
    if kind > 2:
        for j in range(left, i):
            l[tang[j]] -= 1
            if l[tang[j]] == 0:
                kind -= 1
                left = j + 1
                break
    right = i
    answer = max(answer, right - left + 1)

print(answer)