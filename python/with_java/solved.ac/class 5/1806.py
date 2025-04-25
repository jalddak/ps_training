n, m = map(int, input().split())
nums = list(map(int, input().split()))

minLen = n + 1
sums = [0]
for i in range(n):
    sums.append(sums[-1] + nums[i])

l, r = 0, 1

while r <= n and l != r and minLen > 1:
    if sums[r] - sums[l] >= m:
        minLen = min(minLen, r - l)
        l += 1
    else:
        r += 1

answer = minLen if minLen != n + 1 else 0
print(answer)