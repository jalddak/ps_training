import heapq

import sys
sys.stdin = open('./python/with_java/swea/input.txt', 'r')

tcCnt = int(input())

answer = []

def distance(ay, ax, by, bx):
    return ((ay - by) ** 2 + (ax - bx) ** 2) ** 0.5

def findParent(parent, x):
    if parent[x] != x:
        return findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for tc in range(1, tcCnt + 1):
    sb = "#" + str(tc) + " "
    n = int(input())

    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    e = float(input())

    heap = []
    for i in range(n):
        for j in range(i+1, n):
            l = distance(ys[i], xs[i], ys[j], xs[j])
            heapq.heappush(heap, (l, i, j))
    
    visited = set()
    parent = [i for i in range(n)]

    result = 0
    while heap:
        l, i, j = heapq.heappop(heap)

        if findParent(parent, i) == findParent(parent, j):
            continue
        unionParent(parent, i, j)
        result += e * (l ** 2)
    
    result = int(result + 0.5)
    sb += str(result)
    answer.append(sb)



for a in answer:
    print(a)