from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pVisited = [[False for _ in range(m)] for _ in range(n)]
        aVisited = [[False for _ in range(m)] for _ in range(n)]
        pStack = []
        aStack = []

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    pVisited[i][j] = True
                    pStack.append((i, j))
                if i == n-1 or j == m-1:
                    aVisited[i][j] = True
                    aStack.append((i, j))

        dfs(heights, pVisited, pStack, n, m)
        dfs(heights, aVisited, aStack, n, m)

        result = []
        for i in range(n):
            for j in range(m):
                if pVisited[i][j] and aVisited[i][j]:
                    result.append([i, j])
        return result

def dfs(heights, visited, stack, n, m):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    while stack:
        y, x = stack.pop()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and heights[ny][nx] >= heights[y][x]:
                visited[ny][nx] = True
                stack.append((ny, nx))
    
            
        