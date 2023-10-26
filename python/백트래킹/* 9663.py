N = int(input())

row = [0 for _ in range(N)]
result = 0
def solution(num):
    global result, row
    if num == N:
        result += 1
    else:
        for i in range(N):
            check = 0
            for j in range(num):
                if i == row[j] or abs(num-j) == abs(i-row[j]):
                    check = 1
                    break
            if check == 0:
                row[num] = i
                solution(num+1)

solution(0)
print(result)

# 시간초과
# N = int(input())
# board = [[0 for _ in range(N)] for _ in range(N)]

# dy = [-1, -1]
# dx = [-1, 1]

# result = 0
# row_check = [0 for _ in range(N)]

# def solution(board, row, row_check):
#     global result

#     if row == N:
#         result += 1
#     else:
#         for i in range(N):
#             check = 0
#             if row_check[i] == 1:
#                 check = 1
#             else:
#                 for j in range(row):
#                     n = row - j
#                     for d in range(2):
#                         cy = row + dy[d] * n
#                         cx = i + dx[d] * n
#                         if 0 <= cy < N and 0 <= cx < N and board[cy][cx] == 1:
#                             check = 1
#                             break
#                     if check == 1:
#                         break
#             if check == 0:
#                 board[row][i] = 1
#                 row_check[i] = 1
#                 solution(board, row+1, row_check)
#                 board[row][i] = 0
#                 row_check[i] = 0

# solution(board, 0, row_check)
# print(result)