n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = [0] * 3

dy = [0, 0, 0, 1, 1, 1, 2, 2, 2]
dx = [0, 1, 2, 0, 1, 2, 0, 1, 2]

def rc(length, y, x):
    if length == 1:
        return board[y][x]
    
    check = []
    nl = length // 3
    for d in range(9):
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
    print(answer[-1])
    print(answer[0])
    print(answer[1])

if __name__ == "__main__":
    main()
