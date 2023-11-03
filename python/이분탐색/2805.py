N, M = map(int, input().split())

trees = list(map(int, input().split()))
min_height = 0
max_height = max(trees)

while min_height + 1 < max_height:
    middle = (min_height + max_height) // 2
    result = 0
    for t in trees:
        result += t - middle if t > middle else 0
    if result >= M:
        min_height = middle
    else:
        max_height = middle

print(min_height)