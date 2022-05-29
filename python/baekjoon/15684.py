def make_ladder():
    N, M, H = map(int, input().split())
    ladder = [[0 for _ in range(N)] for _ in range(H)]
    for i in range(M):
        y, x = map(int, input().split())
        ladder[y-1][x-1] = 1
        ladder[y-1][x] = -1
    return ladder


def check(ladder):
    for i in range(len(ladder[0])):
        start = i
        for j in range(len(ladder)):
            if ladder[j][i] == 1:
                i += 1
            elif ladder[j][i] == -1:
                i -= 1
        if start != i:
            return -1
    return 1


def draw_row(ladder, combination):
    for i in range(len(combination)):
        y = combination[i][0]
        x = combination[i][1]
        ladder[y][x] = 1
        ladder[y][x+1] = -1
    result = check(ladder)
    if result != 1:
        for i in range(len(combination)):
            y = combination[i][0]
            x = combination[i][1]
            ladder[y][x] = 0
            ladder[y][x+1] = 0
    return result


def main():
    ladder = make_ladder()
    candidates = []
    for i in range(len(ladder)):
        for j in range(len(ladder[i]) - 1):
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                candidates.append((i,j))

    if check(ladder) == 1:
        print(0)
        return 0
    
    for i in range(len(candidates)):
        ladder[candidates[i][0]][candidates[i][1]] = 1
        ladder[candidates[i][0]][candidates[i][1]+1] = -1
        if check(ladder) == 1:
            print(1)
            return 1
        ladder[candidates[i][0]][candidates[i][1]] = 0
        ladder[candidates[i][0]][candidates[i][1]+1] = 0
    
    for i in range(len(candidates)):
        for j in range(i, len(candidates)):
            if candidates[i][0] == candidates[j][0] and candidates[i][1] + 1 == candidates[j][1]:
                continue
            if draw_row(ladder, [candidates[i], candidates[j]]) == 1:
                print(2)
                return 2

    for i in range(len(candidates)):
        for j in range(i, len(candidates)):
            if candidates[i][0] == candidates[j][0] and candidates[i][1] + 1 == candidates[j][1]:
                continue
            for k in range(j, len(candidates)):
                if candidates[j][0] == candidates[k][0] and candidates[j][1] + 1 == candidates[k][1]:
                    continue
                if draw_row(ladder, [candidates[i], candidates[j], candidates[k]]) == 1:
                    print(3)
                    return 3

    print(-1)
    return -1
    

if __name__ == '__main__':
    main()