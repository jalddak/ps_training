import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    m = int(input())
    if m != 0:
        arr.append(m)
    else:
        arr.pop()
print(sum(arr))