# dfs 문제 풀땐 아래 sys.setrecursionlimit 를 필수로 활용하자.
import sys
sys.setrecursionlimit(5000)

def dfs(depth, k, n, m, x, y, r, c, route):
    if depth == k:
        if (x, y) == (r, c):
            return route
        else:
            return ''
        
    if (abs(x-r) + abs(y-c)) > k - depth:
        return ''
    
    # 하 왼 우 상 / x : 세로 / y : 가로
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    d = ['d', 'l', 'r', 'u']
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nd = d[i]
        if 0 <= nx < n and 0 <= ny < m:
            result = dfs(depth+1, k, n, m, nx, ny, r, c, route+nd)
            if result != '':
                return result
    
    return ''

def solution(n, m, x, y, r, c, k):
    if (abs(x-r) + abs(y-c)) % 2 != k % 2:
        return "impossible"
    answer = dfs(0, k, n, m, x-1, y-1, r-1, c-1, '')
    if answer == '':
        return "impossible"
    return answer