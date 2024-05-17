import heapq


def spread(time, inactive, wait, visited):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    candidate = {}
    while wait:
        t, loca = wait.pop()
        y, x = loca
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if (ny, nx) in visited:
                continue
            candidate[(ny, nx)] = max(candidate.get((ny, nx), 0), t)
    for key in candidate:
        heapq.heappush(inactive, (time + candidate[key], candidate[key], key))
        visited.add(key)


def activate(time, inactive, active, wait):
    while inactive and inactive[0][0] == time:
        check, t, loca = heapq.heappop(inactive)
        heapq.heappush(active, (time + t))
        wait.append((t, loca))


def die(time, active):
    while active and active[0] == time:
        heapq.heappop(active)


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    init = [list(map(int, input().split())) for _ in range(N)]
    inactive = []
    active = []
    wait = []
    visited = set()
    time = 0
    for i in range(N):
        for j in range(M):
            if init[i][j] == 0:
                continue
            heapq.heappush(inactive, (init[i][j], init[i][j], (i, j)))
            visited.add((i, j))

    while time < K:
        time += 1
        spread(time, inactive, wait, visited)
        activate(time, inactive, active, wait)
        die(time, active)

    answer = len(inactive) + len(active)
    print("#" + str(t) + " " + str(answer))
