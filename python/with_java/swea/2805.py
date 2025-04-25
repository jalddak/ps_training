tcCnt = int(input())

answer = []
for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    n = int(input())

    board = [list(map(int, list(input()))) for _ in range(n)]
    
    mid = n // 2
    result = 0
    for i in range(n):
        rg = mid - abs(i - mid)
        result += sum(board[i][mid - rg :mid+1 + rg])
    
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)
    