import sys
input = sys.stdin.readline

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]


visited = [False for _ in range(n)]
count = 0
stack = [(0, 0)]
result = 0

def calc_dist(one, two):
    return (one[0] - two[0]) ** 2 + (one[1] - two[1]) ** 2

while len(stack) != 0 and count < n:
    dist, index = stack.pop()
    if visited[index]:
        continue
    result += dist ** 0.5
    visited[index] = True
    count += 1
    for i in range(n):
        if visited[i]:
            continue
        n_dist = calc_dist(stars[index], stars[i])
        stack.append((n_dist, i))
        stack.sort(key=lambda x:-x[0])

print(format(result, ".2f"))