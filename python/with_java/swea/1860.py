tcCnt = int(input())

answer = []
for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    n, m, k = map(int, input().split())
    secs = list(map(int, input().split()))
    secs.sort(reverse=True)
    max_s = max(secs)
    cur = 0
    result = "Possible"
    for i in range(max_s + 1):
        if i % m == 0 and i != 0:
            cur += k
        if secs[-1] <= i:
            cur -= 1
            secs.pop()
        if cur < 0:
            result = "Impossible"
            break
    
    sb += result
    answer.append(sb)

for a in answer:
    print(a)