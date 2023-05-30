turn = list(map(int, input().split()))
board = [[i*2 for i in range(22)]]
board[0][-1] = 0
board.append([10, 13, 16, 19])
board.append([20, 22, 24])
board.append([30, 28, 27, 26])
board.append([25, 30, 35])

def move(loca, l, n):
    global board

    result = False
    nl = list(l)
    if l == (0, 5):
        nl = [1, 0]
    elif l == (0, 10):
        nl = [2, 0]
    elif l == (0, 15):
        nl = [3, 0]
    while n != 0:
        if nl == [0, 21]:
            break
        n -= 1
        nl[1] += 1
        if nl[0] == 1 or nl[0] == 2 or nl[0] == 3:
            if nl[1] == len(board[nl[0]]):
                nl = [4, 0]
        elif nl == [4, 3]:
            nl = [0, 20]

    score = board[nl[0]][nl[1]]
    nl = tuple(nl)
    if nl not in loca:
        if nl != (0, 21):
            loca.append(nl)
        result = True
        i = loca.index(l)
        loca.pop(i)

    return result, score


def dfs(depth, loca, score):
    global turn, board

    if depth == 10:
        return score

    n = turn[depth]
    rm_dupl = list(set(loca))
    candidate = []
    for l in rm_dupl:
        copy = loca[:]
        moving, plus = move(copy, l, n)
        if moving:
            candidate.append(dfs(depth+1, copy, score+plus))
    max_num = max(candidate)
    return max_num


def main():
    global turn
    loca = [(0, 0), (0, 0), (0, 0), (0, 0)]
    result = dfs(0, loca, 0)
    print(result)

if __name__ == '__main__':
    main()