# DFS

# import sys
# input = sys.stdin.readline

N, M = list(map(int, input().split()))

tree = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = list(map(int, input().split()))
    tree[B].append(A)

max_cnt = 0
result = []

for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    cnt = 0
    if not visited[i]:
        visited[i] = True
        cnt += 1
        stack = [i]
        while len(stack) != 0:
            n = stack.pop()
            for child in tree[n]:
                if not visited[child]:
                    visited[child] = True
                    cnt += 1
                    stack.append(child)
    if cnt > max_cnt:
        max_cnt = cnt
        result = [i]
    elif cnt == max_cnt:
        result.append(i)

for n in result:
    print(n, end=' ')
print()