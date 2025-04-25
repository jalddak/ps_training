answer = []

for tc in range(1, 11):
    sb = "#" + str(tc) + " "
    n = int(input())
    board = [list(input()) for _ in range(8)]

    result = 0
    for i in range(8):
        for j in range(n-1, 8):
            l = j - (n - 1)
            r = j

            rowCheck = True
            colCheck = True
            while l <= r and (rowCheck or colCheck):
                if board[i][l] != board[i][r]:
                    rowCheck = False
                if board[l][i] != board[r][i]:
                    colCheck = False
                l += 1
                r -= 1
            
            result += 1 if rowCheck else 0
            result += 1 if colCheck else 0
    
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)