# bfs 우선순위큐 식으로 풀면 

# 4 5
# 5 5 5 5 5
# 5 100 1 1 100
# 5 5 5 5 5
# 5 5 5 5 5

# 이 반례에서 오류가 난다.
# 이걸 해결해주거나 dfs 형식으로 풀어야한다.

global n, m, board, result
nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = 0

def check(y, x):
    global n, m, result
    # 북 동 남 서
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    candidates = [[board[y][x], [y, x]]]
    four = []
    maxnum = 0
    while len(four) < 4:
        candidates.sort(key=lambda x:(-x[0]), reverse=True)
        candidate = candidates.pop()[1]
        if candidate in four:
            continue
        four.append(candidate)
        maxnum += board[candidate[0]][candidate[1]]
        for i in range(4):
            ny = candidate[0] + dy[i]
            nx = candidate[1] + dx[i]
            if ny < 0 or ny > n-1 or nx < 0 or nx > m-1:
                continue
            cc = [board[ny][nx], [ny,nx]]
            if cc in candidates or [ny,nx] in four:
                continue
            candidates.append([board[ny][nx], [ny,nx]])
    if result < maxnum:
        result = maxnum


def main():
    global n, m
    for i in range(n):
        for j in range(m):
            check(i, j)


if __name__ == '__main__':
    main()
    print(result)
