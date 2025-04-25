result = 0

def check(y, x, info):
    for i in range(y):
        if abs(i - y) == abs(info[i] - x):
            return True
    return False

def dfs(depth, n, info, visited):
    global result
    if depth == n:
        result += 1
        return
    
    for i in range(n):
        if visited[i] or check(depth, i, info):
            continue
        info[depth] = i
        visited[i] = True
        dfs(depth + 1, n, info, visited)
        visited[i] = False
        info[depth] = -1

def main():
    global result
    answer = []

    tcCnt = int(input())
    for tc in range(1, tcCnt+1):
        result = 0
        sb = "#" + str(tc) + " "
        n = int(input())
        info = [-1 for _ in range(n)]

        dfs(0, n, info, [False for _ in range(n)])
        sb += str(result)
        answer.append(sb)
    
    for a in answer:
        print(a)

if __name__ == '__main__':
    main()
