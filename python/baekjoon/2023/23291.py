from collections import deque

N, K = list(map(int, input().split()))
fishbowl = list(map(int, input().split()))


def minplus(fishbowl):
    global N

    minnum = min(fishbowl)
    for i in range(N):
        if minnum == fishbowl[i]:
            fishbowl[i] += 1


def control(board):
    # increase decrease table
    idt = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    dy = [0, 1]
    dx = [1, 0]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                for k in range(2):
                    ay = i + dy[k]
                    ax = j + dx[k]
                    if 0 <= ay < len(board) and 0 <= ax < len(board[i]) and board[ay][ax] != 0:
                        dif = abs(board[i][j] - board[ay][ax])
                        if dif // 5 > 0:
                            if board[i][j] > board[ay][ax]:
                                idt[i][j] -= dif // 5
                                idt[ay][ax] += dif // 5
                            elif board[i][j] < board[ay][ax]:
                                idt[i][j] += dif // 5
                                idt[ay][ax] -= dif // 5
    result = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                board[i][j] += idt[i][j]
                result.append(board[i][j])
    
    return result


def rotate90(fishbowl):
    global N

    ls = []
    for i in range(N):
        ls.append([fishbowl[i]])
    
    effect = 1
    while True:
        ups = ls[:effect]
        ls = ls[effect:]
        effect = len(ups[0])
        if len(ls) >= effect:
            for i in range(len(ups)):
                for j in range(len(ups[i])):
                    ls[j].insert(1, ups[i][j])
        else:
            break

    ls = ups + ls
    board = [[0 for _ in range(len(ls[0]))] for _ in range(len(ls))]
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            board[i][j] = ls[i][j]

    fishbowl = control(board)
    return fishbowl


def rotate180(fishbowl):
    copy = fishbowl[:]
    length = len(copy)
    one = copy[:length//2]
    two = copy[length//2:]
    one.reverse()
    oo = one[:length//4]
    ot = one[length//4:]
    oo.reverse()
    to = two[:length//4]
    tt = two[length//4:]
    to.reverse()

    ls = [to, oo, ot, tt]
    ls.reverse()
    board = [[0 for _ in range(len(ls))] for _ in range(len(ls[0]))]
    for i in range(len(ls[0])):
        for j in range(len(ls)):
            board[i][j] = ls[j][i]

    fishbowl = control(board)
    return fishbowl
    

def main():
    global N, K, fishbowl

    cnt = 0
    while True:
        cnt += 1
        minplus(fishbowl)
        fishbowl = rotate90(fishbowl)
        fishbowl = rotate180(fishbowl)
        if max(fishbowl) - min(fishbowl) <= K:
            break
    print(cnt)


if __name__ == '__main__':
    main()