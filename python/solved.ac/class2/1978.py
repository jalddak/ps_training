N = int(input())

l = list(map(int, input().split()))

result = 0
for n in l:
    check = True
    if n == 1:
        check = False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            check = False
            break
    if check:
        result += 1

print(result)