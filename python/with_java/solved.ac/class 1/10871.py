n, x = map(int, input().split())
l = list(map(int, input().split()))
answer = []
for m in l:
    if m < x:
        answer.append(m)
print(*answer)