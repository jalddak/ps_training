import sys
def input():
    return sys.stdin.readline().strip()
sys.setrecursionlimit(10**6)

t = int(input())

def recursion(nums, dp, visited, cur, depth):
    if dp[cur]:
        return depth
    if cur in visited:
        return visited[cur]
    visited[cur] = depth
    result = recursion(nums, dp, visited, nums[cur], depth+1)
    dp[cur] = True
    return result
    
answer = []
for _ in range(t):
    n = int(input())
    nums = list(map(lambda x:x-1, map(int, input().split())))
    dp = [False for _ in range(n)]

    cnt = 0
    for i in range(n):
        if dp[i]:
            continue
        visited = {}
        cnt += recursion(nums, dp, visited, i, 0)
        
    
    answer.append(cnt)

print("\n".join(map(str, answer)))