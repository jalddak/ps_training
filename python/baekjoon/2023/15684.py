from collections import deque

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

    selects = deque([])
    for i in range(len(candidates)):
        selects.append(candidates[i])
        a_ladder = add_row(ladder, selects)
        if check(a_ladder) == 1:
            print(1)
            return 0
        selects.pop()
        
    for i in range(len(candidates)-1):
        selects.append(candidates[i])
        for j in range(i+1, len(candidates)):
            if [candidates[j][0], candidates[j][1]-1] not in selects:
                selects.append(candidates[j])
                a_ladder = add_row(ladder, selects)
                if check(a_ladder) == 1:
                    print(2)
                    return 0
                selects.pop()
        selects.pop()
            
    for i in range(len(candidates)-2):
        selects.append(candidates[i])
        for j in range(i+1, len(candidates)-1):
            if [candidates[j][0], candidates[j][1]-1] not in selects:
                selects.append(candidates[j])
                for k in range(j+1, len(candidates)):
                    if [candidates[k][0], candidates[k][1]-1] not in selects:
                        selects.append(candidates[k])
                        a_ladder = add_row(ladder, selects)
                        if check(a_ladder) == 1:
                            print(3)
                            return 0
                        selects.pop()
                selects.pop()
        selects.pop()
        
    print(-1)

    
if __name__ == '__main__':
    main()