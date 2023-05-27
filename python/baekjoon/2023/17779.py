n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def div(y, x, d1, d2):
    global n
    check = [[0 for _ in range(n)] for _ in range(n)]

    # 경계 체크
    for i in range(d1+1):
        for j in range(d2+1):
            check[y+i+j][x-i+j] = 5
    # 1구역
    for i in range(y+d1):
        for j in range(x+1):
            if check[i][j] == 5:
                break
            check[i][j] = 1
    # 2구역
    for j in range(x+1, n):
        for i in range(y+d2+1):
            if check[i][j] == 5:
                break
            check[i][j] = 2
    # 3구역
    for i in range(y+d1, n):
        for j in range(x-d1+d2):
            if check[i][j] == 5:
                break
            check[i][j] = 3
    # 4구역
    for j in range(x-d1+d2, n):
        for i in range(n-1, y+d2, -1):
            if check[i][j] == 5:
                break
            check[i][j] = 4

    return check

def dif_max_min(check, board):
    global n
    one, two, three, four, five = [0, 0, 0, 0, 0]
    for i in range(n):
        for j in range(n):
            if check[i][j] == 1:
                one += board[i][j]
            elif check[i][j] == 2:
                two += board[i][j]
            elif check[i][j] == 3:
                three += board[i][j]
            elif check[i][j] == 4:
                four += board[i][j]
            else:
                five += board[i][j]
    maxnum = max([one, two, three, four, five])
    minnum = min([one, two, three, four, five])
    return maxnum - minnum


def main():
    global n, board
    
    least = n*n*100
    for y in range(n-2):
        for x in range(1, n-1):
            for d1 in range(1, n-1):
                for d2 in range(1, n-1):
                    if 0 <= y+d1+d2 < n and 0 <= x-d1 and x+d2 < n:
                        check = div(y, x, d1, d2)
                        dif = dif_max_min(check, board)
                        least = min(least, dif)
    print(least)

if __name__ == '__main__':
    main()