# 플워
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    board[i][i] = 1

route = list(map(lambda x:x-1, map(int, input().split())))

for r in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][r] == 1 and board[r][j] == 1:
                board[i][j] = 1

check = board[route[0]]
for n in route:
    if check[n] == 0:
        print("NO")
        exit()
print("YES")

# 유니온 파인드
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
route = list(map(lambda x:x-1, map(int, input().split())))

roots = [i for i in range(N)]

def find(n):
    global roots
    if n != roots[n]:
        roots[n] = find(roots[n])
    return roots[n]

for i in range(N):
    for j in range(i, N):
        if board[i][j] == 1:
            rooti = find(i)
            rootj = find(j)
            if rooti == rootj:
                continue
            if rooti < rootj:
                roots[rootj] = rooti
            else:
                roots[rooti] = rootj

root = find(route[0])
for n in route:
    if find(n) != root:
        print("NO")
        exit()
print("YES")

# bfs_dfs 가능
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
route = list(map(lambda x:x-1, map(int, input().split())))

candidate = set()
stack = [route[0]]
candidate.add(route[0])
while stack:
    n = stack.pop()
    for i in range(N):
        if board[n][i] == 1 and i not in candidate:
            candidate.add(i)
            stack.append(i)

if candidate & set(route) == set(route):
    print("YES")
else:
    print("NO")