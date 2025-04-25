tcCnt = int(input())

answer = []

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    
    temp = set()
    board = [list(map(int, input().split())) for _ in range(4)]

    for i in range(4):
        for j in range(4):

            stack = [(i, j, [])]
            while stack:
                y, x, info = stack.pop()
                if len(info) == 7:
                    temp.add("".join(map(str, info)))
                    continue

                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    nInfo = info[:]
                    if ny >= 4 or ny < 0 or nx >= 4 or nx < 0:
                        continue
                    nInfo.append(board[ny][nx])
                    stack.append((ny, nx, nInfo))


    result = len(temp)
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)