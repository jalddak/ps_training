# DFS

bottles = list(map(int, input().split()))
A, B, C = bottles

visited = [[[False for _ in range(C+1)] for _ in range(B+1)] for _ in range(A+1)]

    # visited = [[0]*(b+1) for _ in range(a+1)]
    # graph[i][j]에는 첫 번째 물통에 i, 두 번째 물통에 j만큼의 물이 들어있는 경우를 말한다.
    # 같은 조합을 여러 번 탐색하지 않기 위해 도입
    # 이 때 세 번째 물통의 양은 c - (i+j)로 구할 수 있음

    # 위 내용은 다른사람코드를 참고함. 이러면 공간복잡도는 줄어들것 같음. 시간복잡도는 모르겠다.

stack = [[0, 0, C]]
visited[0][0][C] = True

result = []
while len(stack) != 0:
    now = stack.pop()
    if now[0] == 0:
        result.append(now[-1])
    
    for i in range(len(now)):
        if now[i] != 0:
            for j in range(len(now)):
                if i == j:
                    continue
                able = bottles[j] - now[j]
                move = able if now[i] >= able else now[i]
                next = now[:]
                next[j] += move
                next[i] -= move
                na, nb, nc = next
                if not visited[na][nb][nc]:
                    visited[na][nb][nc] = True
                    stack.append(next)

result.sort()
for n in result:
    print(n, end=' ')
print()