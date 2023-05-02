from collections import deque

global n, k, l, board, cmd, sec, s, dy, dx
sec = 0
cmd = deque([])
s = deque([[0, 0]])
# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def move(d):
    global n, k, l, board, cmd, sec, s, dy, dx
    while True:
        sec += 1
        h_loca = s[-1]
        n_h_loca = [h_loca[0] + dy[d], h_loca[1] + dx[d]]
        if n_h_loca[0] >= 0 and n_h_loca[0] < n and n_h_loca[1] >= 0 and n_h_loca[1] < n and board[n_h_loca[0]][n_h_loca[1]] != 2:
            if board[n_h_loca[0]][n_h_loca[1]] != 1:
                t_loca = s.popleft()
                board[t_loca[0]][t_loca[1]] = 0
            board[n_h_loca[0]][n_h_loca[1]] = 2
            s.append(n_h_loca)
            if len(cmd) >= 1 and cmd[0][0] == sec:
                rotate = cmd.popleft()[1]
                if rotate == 'L':
                    d -= 1
                    if d < 0:
                        d += 4
                else:
                    d += 1
                    if d > 3:
                        d -= 4
        
        else:
            return sec


def main():
    global n, k, l, board, cmd
    n = int(input())
    k = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        a_loca = list(map(int, input().split()))
        board[a_loca[0]-1][a_loca[1]-1] = 1
    l = int(input())
    for _ in range(l):
        command = input().split()
        sec = int(command[0])
        d = command[1]
        cmd.append([sec, d])
    board[0][0] = 2
    move(1)

if __name__ == '__main__':
    main()
    print(sec)