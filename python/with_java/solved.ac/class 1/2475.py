import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
answer = 0
for n in nums:
    answer += n*n
answer %= 10

print(answer)