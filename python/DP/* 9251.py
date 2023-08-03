f = input()
s = input()

board = [[0 for _ in range(len(f)+1)] for _ in range(len(s)+1)]
for i in range(1, len(s)+1):
    for j in range(1, len(f)+1):
        if s[i-1] == f[j-1]:
            board[i][j] = board[i-1][j-1] + 1
        else:
            board[i][j] = max(board[i-1][j], board[i][j-1])

print(board[len(s)][len(f)])


# 내가 생각한 방법은 안됨
# dp = {'' : ['', -1]}
# for char in f:
#     ndp = {}
#     for key in dp:
#         ndp[key] = dp[key]
#     for key in dp:
#         cs, index = dp[key]
#         for j in range(index+1, len(s)):
#             if char == s[j]:
#                 if char not in ndp or len(ndp[char][0]) < len(cs+char):
#                     ndp[char] = [cs+char, j]
#     dp = ndp

# max_len = 0
# for key in dp:
#     max_len = max(max_len, len(dp[key][0]))
# print(max_len)