def check(board, n, x, y, result):
    flag = True
    before = board[y][x]
    for i in range(n):
        for j in range(n):
            if board[y+i][x+j] != before:
                flag = False
                break
        if not flag:
            break
    if flag:
        result[board[y][x]] += 1
    else:
        check(board, n//2, x, y, result)
        check(board, n//2, x + n//2, y, result)
        check(board, n//2, x, y + n//2, result)
        check(board, n//2, x + n//2, y + n//2, result)

def main():
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    result = [0, 0]
    check(board, n, 0, 0, result)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()