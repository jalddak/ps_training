result = []
for round in range(10):
    rstr = "#" + str(round+1) + " "
    dump_cnt = int(input())
    box_heights = list(map(int, input().split()))
    for _ in range(dump_cnt):
        max_h = max(box_heights)
        min_h = min(box_heights)
        box_heights[box_heights.index(max_h)] -= 1
        box_heights[box_heights.index(min_h)] += 1
    rstr += str(max(box_heights) - min(box_heights))
    result.append(rstr)

for r in result:
    print(r)