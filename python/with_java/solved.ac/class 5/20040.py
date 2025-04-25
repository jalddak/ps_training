import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parents = [i for i in range(n)]

answer = 0

def find(node):
    return node if parents[node] == node else find(parents[node])

# check = [list(map(int, input().split())) for _ in range(m)]
# for i in range(m):
#     l, r = check[i]
#     lRoot = find(l)
#     rRoot = find(r)
#     if lRoot == rRoot:
#         answer = i + 1
#         break
#     if lRoot < rRoot:
#         parents[rRoot] = lRoot
#     else:
#         parents[lRoot] = rRoot

flag = False
for i in range(m):
    l, r = map(int, input().split())
    if flag:
        continue
    lRoot = find(l)
    rRoot = find(r)
    if lRoot == rRoot:
        answer = i + 1
        flag = True
        break
    if lRoot < rRoot:
        parents[rRoot] = lRoot
    else:
        parents[lRoot] = rRoot


print(answer)