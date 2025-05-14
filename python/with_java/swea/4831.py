tcCnt = int(input())

answer = []
for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    k, n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.reverse()

    result = 0
    x = 0
    while x + k < n:
        x += k
        temp = -1
        while nums:
            y = nums.pop()
            if x >= y:
                temp = y
            else:
                nums.append(y)
                break
        if temp != -1:
            result += 1
            x = temp
        else:
            result = 0
            break

    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)