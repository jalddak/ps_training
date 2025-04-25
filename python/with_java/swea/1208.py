from collections import deque

answer = []

for tc in range(1, 11):
    result = "#" + str(tc) + " "
    cnt = int(input())
    heights = list(map(int, input().split()))
    
    for _ in range(cnt):
        max_h = max(heights)
        min_h = min(heights)
        if max_h - min_h <= 1:
            break
        heights[heights.index(max_h)] -= 1
        heights[heights.index(min_h)] += 1

    result += str(max(heights) - min(heights))
    answer.append(result)

for a in answer:
    print(a)