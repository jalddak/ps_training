# DFS

##### 방법 3, pypy3로만 통괴.
N, M = list(map(int, input().split()))

board = [[-1 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    s, t = list(map(lambda x: x-1, list(map(int, input().split()))))
    board[s][t] = 1

for i in range(N):
    board[i][i] = 1

# 플로이드 워셜 에선 가장 첫번째 포문이 미들값 여기서는 k로 하라고 한다. 왜 인진 이해 아직 못함. 걍 그러라니까 그래야지
for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 or (board[i][k] == 1 and board[k][j] == 1):
                board[i][j] = 1

result = 0
for i in range(N):
    flag = 1
    for j in range(N):
        if board[i][j] == 1 or board[j][i] == 1:
            continue
        else:
            flag = 0
    if flag == 1:
        result += 1

print(result)

##### 방법 2, 시간초과 // 다시 해보니까 pypy3로 통과함.
# N, M = list(map(int, input().split()))

# board = [[-1 for _ in range(N)] for _ in range(N)]
# board2 = [[-1 for _ in range(N)] for _ in range(N)]

# for _ in range(M):
#     s, t = list(map(lambda x: x-1, list(map(int, input().split()))))
#     board[s][t] = 1
#     board2[t][s] = 1

# for i in range(N):
#     board[i][i] = 1

# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == 1 or (board[i][k] == 1 and board[k][j] == 1):
#                 board[i][j] = 1
#             if board2[i][j] == 1 or (board2[i][k] == 1 and board2[k][j] == 1):
#                 board2[i][j] = 1

# result = 0
# for i in range(N):
#     flag = 1
#     for j in range(N):
#         if board[i][j] == 1 or board2[i][j] == 1:
#             continue
#         else:
#             flag = 0
#     if flag == 1:
#         result += 1

# print(result)


##### 방법 1, 시간초과
# N, M = list(map(int, input().split()))

# tree = {}
# for _ in range(M):
#     s, t = list(map(int, input().split()))
#     if s not in tree:
#         tree[s] = [t]
#     else:
#         tree[s].append(t)

# l = [set([]) for _ in range(N+1)]
# for i in range(1, N+1):
#     stack = [[i, i]]
#     while len(stack) != 0:
#         now, start = stack.pop()
#         l[now] = l[now] | set([start])
#         l[start] = l[start] | set([now])
#         if now in tree:
#             for n in tree[now]:
#                 stack.append([n, start])

# result = 0
# for i in range(1, N+1):
#     if len(l[i]) == N:
#         result += 1

# print(result)