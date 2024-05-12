def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i]:
            continue
        answer += 1
        stack = [i]
        while stack:
            current = stack.pop()
            visited[current] = True
            for j in range(n):
                if computers[current][j] == 1 and not visited[j]:
                    stack.append(j)
                    visited[j] = True
    return answer