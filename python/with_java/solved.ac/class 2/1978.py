cnt = int(input())
nums = list(map(int, input().split()))

check = [True for _ in range(1001)]
check[0] = False
check[1] = False
for n in range(2, 1001):
    if check[n]:
        for d in range(2*n, 1001, n):
            check[d] = False

answer = 0
for num in nums:
    if check[num]:
        answer += 1

print(answer)