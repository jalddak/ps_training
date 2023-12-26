S = int(input())

from collections import deque
queue = deque([[0, 1, 0]])
visited = set([(1, 0)])

while queue:
    time, view, clip = queue.popleft()
    if view == S:
        print(time)
        break
    time += 1
    if (view, view) not in visited:
        queue.append([time, view, view])
        visited.add((view, view))
    if clip != 0 and (view + clip, clip) not in visited:
        queue.append([time, view + clip, clip])
        visited.add((view + clip, clip))
    if (view-1, clip) not in visited:
        queue.append([time, view-1, clip])
        visited.add((view-1, clip))