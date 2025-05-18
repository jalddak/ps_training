# 무한입력 받는법

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

prefix = []
while True:
    try:
        prefix.append(int(input()))
    except:
        break

result = []
def solution(start_i, end_i):
    global prefix, result

    n = prefix[start_i]
    left_i = start_i + 1
    right_i = end_i + 1
    for i in range(left_i, end_i+1):
        if n < prefix[i]:
            right_i = i
            break

    if left_i <= right_i-1:
        solution(left_i, right_i-1)
    if right_i <= end_i:
        solution(right_i, end_i)
    result.append(prefix[start_i])
    

solution(0, len(prefix)-1)
for r in result:
    print(r)