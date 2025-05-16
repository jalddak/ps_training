tcCnt = int(input())

answer = []

for tc in range(1, tcCnt + 1):
    sb = "#" + str(tc) + " "
    n, m = map(int, input().split())
    info = [[] for _ in range(n + 1)]
    for _ in range(m):
        f, s = map(int, input().split())
        info[f].append(s)
        info[s].append(f)
    
    result = 0
    visited = [False for _ in range(n + 1)]
    for i in range(1, n+1):
        if visited[i]:
            continue
        result += 1
        visited[i] = True
        stack = [i]
        while stack:
            pop = stack.pop()
            for k in info[pop]:
                if visited[k]:
                    continue
                visited[k] = True
                stack.append(k)
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)