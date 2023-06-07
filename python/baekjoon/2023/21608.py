N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
students = {}
for _ in range(N**2):
    student = list(map(int, input().split()))
    students[student[0]] = student[1:]

def find(board, student, likes):
    global N

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    like = 0
    empty = 0
    loca = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                # temp_like, temp_empty
                tl, te = 0, 0
                for k in range(4):
                    ay = i + dy[k]
                    ax = j + dx[k]
                    if 0 <= ay < N and 0 <= ax < N:
                        if board[ay][ax] in likes:
                            tl += 1
                        elif board[ay][ax] == 0:
                            te += 1

                if tl > like:
                    like, empty = tl, te
                    loca = [i, j]
                elif tl == like and te > empty:
                    like, empty = tl, te
                    loca = [i, j]
                elif tl == like and te == empty and len(loca) == 0 or loca[0] > i:
                    like, empty = tl, te
                    loca = [i, j]
                elif tl == like and te == empty and len(loca) == 0 or loca[0] == i and loca[1] > j:
                    like, empty = tl, te
                    loca = [i, j]
    
    board[loca[0]][loca[1]] = student


def satisfy(board, students):
    global N

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    satisfaction = 0

    for i in range(N):
        for j in range(N):
            likes = students[board[i][j]]
            cnt = 0
            for k in range(4):
                ay = i + dy[k]
                ax = j + dx[k]
                if 0 <= ay < N and 0 <= ax < N and board[ay][ax] in likes:
                    cnt += 1
            if cnt > 0:
                satisfaction += 10 ** (cnt-1)
    
    return satisfaction


def main():
    global N, board, students

    for i in students:
        find(board, i, students[i])
    
    result = satisfy(board, students)
    print(result)

if __name__ == '__main__':
    main()