from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        result = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                visited[i][j] = True
                if grid[i][j] == '1':
                    stack = []
                    stack.append((i, j))
                    while stack:
                        y, x = stack.pop()
                        for d in range(4):
                            ny = y + dy[d]
                            nx = x + dx[d]
                            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][nx] == '1':
                                visited[ny][nx] = True
                                stack.append((ny, nx))
                    result += 1
        return result