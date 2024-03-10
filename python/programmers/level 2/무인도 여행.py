def solution(maps):
    answer = []
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            visited[i][j] = True
            if maps[i][j] == 'X':
                continue
            stack = [(i, j)]
            score = int(maps[i][j])
            while stack:
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0<=ny<n and 0<=nx<m and maps[ny][nx] != 'X' and not visited[ny][nx]:
                        score += int(maps[ny][nx])
                        visited[ny][nx] = True
                        stack.append((ny, nx))
            answer.append(score)
            
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer