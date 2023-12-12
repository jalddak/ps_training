import sys
input = sys.stdin.readline

maxdp = [0, 0, 0]
mindp = [0, 0, 0]

N = int(input())
for _ in range(N):
    nums = list(map(int, input().split()))
    nmaxdp = []
    nmaxdp.append(nums[0] + max(maxdp[0], maxdp[1]))
    nmaxdp.append(nums[1] + max(maxdp))
    nmaxdp.append(nums[2] + max(maxdp[1:]))
    maxdp = nmaxdp

    nmindp = []
    nmindp.append(nums[0] + min(mindp[0], mindp[1]))
    nmindp.append(nums[1] + min(mindp))
    nmindp.append(nums[2] + min(mindp[1:]))
    mindp = nmindp

print(max(maxdp), min(mindp))