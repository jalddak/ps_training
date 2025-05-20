tcCnt = int(input())

def recursion(n, b, hs, cur, candidate, start):
    for i in range(start, n):
        next = cur + hs[i]
        if candidate <= next:
            break
        if next < candidate and next >= b:
            candidate = next
            break
        candidate = recursion(n, b, hs, next, candidate, i + 1)

    return candidate
        

answer = []
for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    n, b = map(int, input().split())
    hs = list(map(int, input().split()))
    hs.sort()
    visited = [False for _ in range(n)]
    sums = sum(hs)
    result = recursion(n, b, hs, 0, sums, 0)
    sb += str(result - b)
    answer.append(sb)

for a in answer:
    print(a)