n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]
answer = ""

dy = [0, 0, 1, 1]
dx = [0, 1, 0, 1]

def rc(l, y, x):
    global answer

    flag = True
    temp = board[y][x]
    for i in range(l):
        for j in range(l):
            ty = y + i
            tx = x + j
            if board[ty][tx] != temp:
                flag = False
                break
        if not flag:
            break
    
    if flag:
        answer += str(board[y][x])
        return

    answer += "("
    nl = l // 2
    for d in range(4):
        ny = y + dy[d] * nl
        nx = x + dx[d] * nl
        rc(nl, ny, nx)
    answer += ")"
        


def main():
    global answer

    rc(n, 0, 0)
    print(answer)

if __name__ == "__main__":
    main()