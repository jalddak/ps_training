n = int(input())
s = set(list(map(int, input().split())))
m = int(input())
l = list(map(int, input().split()))
answer = []
for i in range(m):
    if l[i] in s:
        answer.append(1)
    else:
        answer.append(0)

print("\n".join(map(str, answer)))