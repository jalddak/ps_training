import sys

board = [list(map(int, input().split())) for _ in range(3)]

answer = 10

def calc(info):
    global answer

    for h in range(1, 4):
        result = 0
        for num in info:
            result += abs(num-h)
        answer = min(answer, result)
        
for i in range(3):
    row = []
    col = []
    for j in range(3):
        row.append(board[i][j])
        col.append(board[j][i])
    calc(row)
    calc(col)
    
print(answer)

    
            