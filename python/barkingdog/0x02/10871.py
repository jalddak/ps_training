n, x = map(int, input().split())
a = list(map(int, input().split()))

answer = []
for num in a:
    if num < x:
        answer.append(num)

print(" ".join(map(str, answer)))