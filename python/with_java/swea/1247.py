result = 10000
n, hx, hy = 0, 0, 0
csInfo = []
visited = []

def init():
    global result, n, hx, hy, csInfo, visited
    result = 10000
    n, hx, hy = 0, 0, 0
    csInfo = []
    visited = []

def dfs(depth, bx, by, preSum):
    global result, n, hx, hy, csInfo, visited
    if preSum > result:
        return

    if depth == n:
        result = min(result, preSum + abs(bx-hx) + abs(by-hy))
        return

    for i in range(n):
        if visited[i]:
            continue
        nx, ny = csInfo[i]
        nPreSum = preSum + abs(bx-nx) + abs(by-ny)
        visited[i] = True
        dfs(depth+1, nx, ny, nPreSum)
        visited[i] = False

def main():
    global result, n, hx, hy, csInfo, visited
    tcCnt = int(input())

    answer = []
    for tc in range(1, tcCnt + 1):
        sb = "#" + str(tc) + " "
        n = int(input())
        coord = list(map(int, input().split()))
        cx, cy = coord[0:2]
        hx, hy = coord[2:4]
        for i in range(n):
            temp = 4 + i * 2
            csInfo.append(coord[temp:temp+2])
        visited = [False for _ in range(n)]
        dfs(0, cx, cy, 0)
        sb += str(result)
        answer.append(sb)

        init()
    
    for a in answer:
        print(a)

if __name__ == '__main__':
    main()

