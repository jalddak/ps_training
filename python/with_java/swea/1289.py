tcCnt = int(input())

answer = []
for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    bits = input()

    cur = '0'
    result = 0
    for bit in bits:
        if bit != cur:
            result += 1
            cur = bit
    
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)