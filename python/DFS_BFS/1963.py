import sys
input = sys.stdin.readline

T = int(input())
results = []

def check_sosu(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

nums = list(map(str, [i for i in range(10)]))

from collections import deque
for _ in range(T):
    ori, want = input().split()
    ori = list(ori)
    queue = deque([[ori, 0]])
    visited = set(["".join(ori)])

    possible = False
    while queue:
        now, cnt = queue.popleft()
        if "".join(now) == want:
            results.append(cnt)
            possible = True
            break
        for d in range(4):
            for n in nums:
                if d == 0 and n == '0':
                    continue
                if n == now[d]:
                    continue
                next = now[:]
                next[d] = n
                if not check_sosu(int("".join(next))) or "".join(next) in visited:
                    continue
                queue.append([next, cnt+1])
                visited.add("".join(next))

    if not possible:
        results.append("Impossible")

for r in results:
    print(r)


# 소수 찾는법 더 빠르게: 에라어쩌구 체
import sys
input = sys.stdin.readline

T = int(input())
results = []

prime = [True] * 10000
for i in range(2, 100):
    # 소수인 상태에서 소수의 배수를 체크해줘야 함
    if prime[i] == True:
        # 소수의 배수 체크
        for j in range(i, 10000, i):
            prime[j] = False

nums = list(map(str, [i for i in range(10)]))

from collections import deque
for _ in range(T):
    ori, want = input().split()
    ori = list(ori)
    queue = deque([[ori, 0]])
    visited = set(["".join(ori)])

    possible = False
    while queue:
        now, cnt = queue.popleft()
        if "".join(now) == want:
            results.append(cnt)
            possible = True
            break
        for d in range(4):
            for n in nums:
                if d == 0 and n == '0':
                    continue
                if n == now[d]:
                    continue
                next = now[:]
                next[d] = n
                if not prime[int("".join(next))] or "".join(next) in visited:
                    continue
                queue.append([next, cnt+1])
                visited.add("".join(next))

    if not possible:
        results.append("Impossible")

for r in results:
    print(r)