n = int(input())
l = list(map(int, input().split()))
can = int(input())

min_a = can // n
max_a = max(l)

while min_a <= max_a:
    mid_a = (min_a + max_a) // 2
    temp = 0
    for a in l:
        if a <= mid_a:
            temp += a
        else:
            temp += mid_a
    if temp <= can:
        min_a = mid_a + 1
    else:
        max_a = mid_a - 1
    
print(max_a)