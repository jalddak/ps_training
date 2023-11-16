N = int(input())

l = list(map(int, input().split()))
d = {}

for n in l:
    if n not in d:
        d[n] = 1
    else:
        d[n] += 1

N = int(input())
l = list(map(int, input().split()))

for n in l:
    if n not in d:
        print(0, end=" ")
    else:
        print(d[n], end=" ")

print()