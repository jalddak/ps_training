
def pow(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n
    half = pow(n, p//2)
    result = half ** 2
    if p % 2 != 0:
        result *= n
    return result

answer = []

tcCnt = 10
for _ in range(1, tcCnt + 1):
    tc = int(input())
    sb = "#" + str(tc) + " "
    
    n, p = map(int, input().split())
    result = pow(n, p)
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)