import heapq

# import sys
# sys.stdin = open('./python/with_java/swea/input.txt', 'r')

tcCnt = int(input())

answer = []

def distance(ay, ax, by, bx):
    return ((ay - by) ** 2 + (ax - bx) ** 2) ** 0.5

for tc in range(1, tcCnt + 1):
    sb = "#" + str(tc) + " "
    n = int(input())

    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    e = float(input())

    info = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            l = distance(ys[i], xs[i], ys[j], xs[j])
            info[i].append((l, j))
            info[j].append((l, i))
    
    heap = [(0, 0)]
    visited = [False for _ in range(n)]

    result = 0
    while heap:
        l, loca = heapq.heappop(heap)

        if visited[loca]:
            continue
        visited[loca] = True
        result += e * (l ** 2)
        for nl, nLoca in info[loca]:
            heapq.heappush(heap, (nl, nLoca))
    
    result = int(result + 0.5)
    sb += str(result)
    answer.append(sb)



for a in answer:
    print(a)