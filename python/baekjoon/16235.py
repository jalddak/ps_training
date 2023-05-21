from collections import deque

# n : 땅 크기 / m : 나무 갯수 / k : 햇수 / land : 땅 정보
n, m, k = map(int, input().split())
land = [[ 5 for _ in range(n)] for _ in range(n)]

# a : 추가하는 양분 양 정보
a = [list(map(int, input().split())) for _ in range(n)]

# 나무 정보 : y, x, 나이
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    y, x, old = map(int, input().split())
    trees[y-1][x-1].append(old)

def spring(n, land, trees):
    dead = []
    for i in range(n):
        for j in range(n):
            if len(trees[i][j]) != 0:
                trees[i][j].sort()
                for k in range(len(trees[i][j])):
                    if trees[i][j][k] <= land[i][j]:
                        land[i][j] -= trees[i][j][k]
                        trees[i][j][k] += 1
                    else:
                        dead.append([i, j, k])
                        break
    return dead

def summer(dead, land, trees):
    for d in dead:
        y, x, index = d[0], d[1], d[2]
        # dt : dead trees
        dt = trees[y][x][index:]
        trees[y][x] = trees[y][x][:index]
        for old in dt:
            land[y][x] += (old // 2)

def autumn(n, trees):
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(n):
        for j in range(n):
            if len(trees[i][j]) != 0:
                # 번식하는 나무의 수
                cnt = 0
                for old in trees[i][j]:
                    if old % 5 == 0:
                        cnt += 1
                for k in range(8):
                    ay = i + dy[k]
                    ax = j + dx[k]
                    if 0 <= ay < n and 0 <= ax < n:
                        for _ in range(cnt):
                            trees[ay][ax].append(1)

def winter(n, a, land):
    for i in range(n):
        for j in range(n):
            land[i][j] += a[i][j]

def main():
    global n, m, k, land, a, trees
    for _ in range(k):
        dead = spring(n, land, trees)
        summer(dead, land, trees)
        autumn(n, trees)
        winter(n, a, land)
    
    result = 0
    for i in range(n):
        for j in range(n):
            if len(trees[i][j]) != 0:
                result += len(trees[i][j])
    print(result)

if __name__ == '__main__':
    main()