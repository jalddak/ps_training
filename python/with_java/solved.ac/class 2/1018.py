def minCheck(board):
    cnt = 0
    for i in range(1, 8):
        temp = 'W' if board[i-1][0] == 'B' else 'B'
        if temp != board[i][0]:
            board[i][0] = temp
            cnt += 1
        
    for j in range(1, 8):
        for i in range(8):
            temp = 'W' if board[i][j-1] == 'B' else 'B'
            if temp != board[i][j]:
                board[i][j] = temp
                cnt += 1
    result = min(cnt, 64-cnt)
    return result


def main():
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    chess = []
    answer = n * m
    for i in range(n-8+1):
        sy = i
        for j in range(m-8+1):
            sx = j
            for k in range(8):
                chess.append(board[sy+k][sx:sx+8])
            answer = min(answer, minCheck(chess))
            chess = []
    print(answer)

if __name__ == "__main__":
    main()