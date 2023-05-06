first_row = list(map(int, input().split()))
n = first_row[0]
m = first_row[1]

second_row = list(map(int, input().split()))
r = second_row[0]
c = second_row[1]
d = second_row[2]
# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = 0

def clean():
    global n, m, r, c, d, dy, dx, board, result
    while True:
        if board[r][c] == 0:
            board[r][c] = 2 # 청소하면 2
            result += 1
        check = 0
        for i in range(4):
            nr = r + dy[i]
            nc = c + dx[i]
            if nr >= 0 and nr < n and nc >= 0 and nc < m:
                if board[nr][nc] == 0:
                    check = 1
                    break
        if check == 0:
            back = d + 2
            if back > 3:
                back -= 4
            br = r + dy[back]
            bc = c + dx[back]
            if br >= 0 and br < n and bc >= 0 and bc < m:
                if board[br][bc] != 1:
                    r = br
                    c = bc
                    continue
                break
            break
        if check == 1:
            for _ in range(n):
                d = d - 1
                if d < 0:
                    d += 4
                nr = r + dy[d]
                nc = c + dx[d]
                if nr >= 0 and nr < n and nc >= 0 and nc < m:
                    if board[nr][nc] == 0:
                        r = nr
                        c = nc
                        break
    
if __name__ == '__main__':
    clean()
    print(result)

    
