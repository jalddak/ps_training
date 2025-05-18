N = int(input())
k = int(input())

start, end = 1, N**2

result = 0
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N+1):
        temp += min(mid//i, N)
    
    if temp >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)