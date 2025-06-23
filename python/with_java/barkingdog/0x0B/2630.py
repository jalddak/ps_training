n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = [0] * 2

dy = [0, 0, 1, 1]
dx = [0, 1, 0, 1]

def rc(length, y, x):
    if length == 1:
        return board[y][x]
    
    check = []
    nl = length // 2
    for d in range(4):
        ny = y + dy[d] * nl
        nx = x + dx[d] * nl
        check.append(rc(nl, ny, nx))
    
    if len(set(check)) == 1 and check[0] != 2:
        return check[0]

    for num in check:
        if num == 2:
            continue
        answer[num] += 1
    
    return 2
    
def main():
    result = rc(n, 0, 0)
    if result != 2:
        answer[result] += 1
    print(answer[0])
    print(answer[1])

if __name__ == "__main__":
    main()
