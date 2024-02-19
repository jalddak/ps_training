import sys
input = sys.stdin.readline

answer = 2000 * 2000
N, M = map(int, input().split())

dots = [[] for _ in range(M+1)]

for _ in range(N):
    x, y, c = map(int, input().split())
    dots[c].append((x, y))

def check_area(maxs, mins):
    global answer
    area = (maxs[0] - mins[0]) * (maxs[1] - mins[1])
    if area >= answer:
        return answer
    return area

def recursion(depth, maxs, mins):
    global answer
    for x, y in dots[depth]:
        nmaxs = [max(maxs[0], x), max(maxs[1], y)]
        nmins = [min(mins[0], x), min(mins[1], y)]
        current_area = check_area(nmaxs, nmins)
        if current_area != answer:
            if depth == M:
                answer = current_area
            else: recursion(depth+1, nmaxs, nmins)
        

recursion(1, [-1000, -1000], [1000, 1000])
print(answer)