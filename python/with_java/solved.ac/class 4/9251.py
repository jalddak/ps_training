str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)

board = [[0 for _ in range(len2)] for _ in range(len1)]

for i in range(len1):
    if str1[i] == str2[0]:
        for j in range(i, len1):
            board[j][0] = 1
        break

for i in range(len2):
    if str2[i] == str1[0]:
        for j in range(i, len2):
            board[0][j] = 1
        break

for i in range(1, len1):
    for j in range(1, len2):
        if str1[i] == str2[j]:
            board[i][j] = board[i-1][j-1] + 1
        else:
            board[i][j] = max(board[i-1][j], board[i][j-1])

print(board[len1-1][len2-1])