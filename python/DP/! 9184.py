# 언제 끝날지 모르는 코드는 input을 무조건 sys.stdin.readline으로 받아오는게 맞는 거 같다. 아닌 경우에도 그냥 이제 이렇게 입력 받는게 좋을듯.

import sys
input = sys.stdin.readline

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    global dp
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if dp[a][b][c] != 0:
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

while True:
    a, b, c = list(map(int, input().split()))
    if (a, b, c) == (-1, -1, -1):
        break
    print("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(w(a, b, c)))
