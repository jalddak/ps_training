N, M = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]


def blizard(board, d, s):
    global N

    y, x = ((N+1)//2-1, (N+1)//2-1)
    # 총 4가지 방향 ↑, ↓, ←, →가 있고, 정수 1, 2, 3, 4
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]

    for _ in range(s):
        y += dy[d]
        x += dx[d]
        if 0 <= y < N and 0 <= x < N:
            board[y][x] = 0
        else:
            break


# refactoring and bomb
def RandB(board):
    global N

    line = []
    y, x = ((N+1)//2-1, (N+1)//2-1)
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    
    d = 0
    for i in range(1, N):
        for _ in range(2):
            for _ in range(i):
                y += dy[d]
                x += dx[d]
                line.append(board[y][x])
            d += 1
            if d >= 4:
                d -= 4
    for i in range(N-1):
        y += dy[d]
        x += dx[d]
        line.append(board[y][x])
    
    score = 0
    check = 1
    while check:
        check = 0
        # refactoring
        for i in range(len(line)-1, -1, -1):
            if line[i] == 0:
                line.pop(i)
                line.append(0)
        # bomb search
        num = -1
        cnt = 0
        for i in range(len(line)-1, -1, -1):
            if line[i] not in [0, num]:
                if cnt >= 4:
                    check = 1
                    score += num * cnt
                    for _ in range(cnt):
                        line.pop(i+1)
                        line.append(0)
                num = line[i]
                cnt = 1
            elif num == line[i]:
                cnt += 1
        if cnt >= 4:
            check = 1
            score += num * cnt
            for _ in range(cnt):
                line.pop(0)
                line.append(0)
    
    # 그룹화 하고 라인 재배열
    new_line = []
    
    num = line[0]
    cnt = 1
    for i in range(1, len(line)):
        if num != line[i]:
            new_line.append(cnt)
            new_line.append(num)
            num = line[i]
            cnt = 1
            if num == 0:
                break
        else:
            cnt += 1
    if num != 0:
        new_line.append(cnt)
        new_line.append(num)
    for _ in range(len(line)-len(new_line)):
        new_line.append(0)
    line = new_line[:len(line)]

    y, x = ((N+1)//2-1, (N+1)//2-1)
    d = 0
    index = 0
    for i in range(1, N):
        for _ in range(2):
            for _ in range(i):
                y += dy[d]
                x += dx[d]
                board[y][x] = line[index]
                index += 1
            d += 1
            if d >= 4:
                d -= 4
    for i in range(N-1):
        y += dy[d]
        x += dx[d]
        board[y][x] = line[index]
        index += 1

    return score


def main():
    global N, M, board, commands
    
    score = 0
    for i in range(M):
        d, s = commands[i]
        blizard(board, d, s)
        score += RandB(board)
    print(score)


if __name__ == '__main__':
    main()