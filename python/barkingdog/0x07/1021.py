n, m = map(int, input().split())

from collections import deque
q = deque([i for i in range(1, n+1)])

nums = deque(map(int, input().split()))

result = 0
while nums:
    if q[0] != nums[0]:
        lq = deque(list(q)[:])
        rq = deque(list(q)[:])
        while q[0] != nums[0]:
            result += 1
            lq.rotate(-1)
            rq.rotate(1)
            if lq[0] == nums[0]:
                q = lq
            elif rq[0] == nums[0]:
                q = rq
    if q[0] == nums[0]:
        q.popleft()
        nums.popleft()

print(result)