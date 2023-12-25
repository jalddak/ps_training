N = int(input())
nums = list(map(int, input().split()))

dp = {}
for n in nums:
    temp = []
    for key in dp:
        if n > key and len(dp[key]) > len(temp):
            temp = dp[key][:]
    temp += [n]
    if (n in dp and len(dp[n]) < len(temp)) or n not in dp:
        dp[n] = temp

result = []
for key in dp:
    if len(dp[key]) > len(result):
        result = dp[key]

print(len(result))
print(" ".join(map(str, result)))