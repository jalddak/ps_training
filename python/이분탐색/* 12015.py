# LIS 알고리즘

N = int(input())
l = list(map(int, input().split()))

result = [l[0]]

for n in l[1:]:
    if n > result[-1]:
        result.append(n)
    else:
        min_i = 0
        max_i = len(result) -1
        while min_i < max_i:
            mid_i = (min_i + max_i) // 2
            if result[mid_i] < n:
                min_i = mid_i + 1
            else:
                max_i = mid_i
        result[min_i] = n

print(len(result))

# bisect 모듈 사용

import bisect

N = int(input())
l = list(map(int, input().split()))

result = [l[0]]
for n in l[1:]:
    if result[-1] < n:
        result.append(n)
    else:
        result[bisect.bisect_left(result, n)] = n

print(len(result))
