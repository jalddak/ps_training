from itertools import combinations

n, m, h = map(int, input().split())
ladder = [[0 for _ in range(n)] for _ in range(h)]
for _ in range(m):
    y, x = map(int, input().split())
    ladder[y-1][x-1] = 1
    ladder[y-1][x] = -1

candidates = []
for i in range(h):
    for j in range(n-1):
        if ladder[i][j] == 0 and ladder[i][j+1] == 0:
            candidates.append([i, j])

def check(ladder):
    global n, h
    for i in range(n):
        start = i
        for j in range(h):
            if ladder[j][i] == 1:
                i += 1
            elif ladder[j][i] == -1:
                i -= 1
        if start != i:
            return 0
    return 1

def add_row(ladder, selects):
    global n, h
    a_ladder = [ladder[i][:] for i in range(h)]
    for s in selects:
        a_ladder[s[0]][s[1]] = 1
        a_ladder[s[0]][s[1]+1] = -1

    return a_ladder


def main():
    global ladder, candidates
    if check(ladder) == 1:
        print(0)
        return 0

    for result in range(1, 4):
        combination = list(combinations(candidates, result))
        for selects in combination:
            temp = 1
            for s in selects:
                if [s[0], s[1] - 1] in selects:
                    temp = 0
                    break
            if temp == 1:
                a_ladder = add_row(ladder, selects)
                if check(a_ladder) == 1:
                    print(result)
                    return 0
    print(-1)

    
if __name__ == '__main__':
    main()