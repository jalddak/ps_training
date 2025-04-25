tcCnt = int(input())

scanner = {}
scanner[211] = 0
scanner[221] = 1
scanner[122] = 2
scanner[411] = 3
scanner[132] = 4
scanner[231] = 5
scanner[114] = 6
scanner[312] = 7
scanner[213] = 8
scanner[112] = 9


answer = []
for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    n, m = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(n)]

    code = 0
    codeLen = 0
    for i in range(n):
        if len(set(board[i])) == 1:
            continue
        
        flag = 0
        num = board[i][0]
        numCnt = 0
        checkNum = 0
        for j in range(m):
            if num == board[i][j]:
                numCnt += 1
                continue
            checkNum *= 10
            checkNum += numCnt
            flag += 1
            if flag == 4:
                flag = 0
                code *= 10
                code += scanner[checkNum % 1000]
                codeLen += 1
                checkNum = 0
            if codeLen == 8:
                break
            num = board[i][j]
            numCnt = 1
        break
    
    result = 0

    candidate = 0
    decoding = 0

    for i in range(8):
        temp = code % 10
        code //= 10
        candidate += temp
        temp *= 3 if i % 2 == 1 else 1
        decoding += temp
    
    if decoding % 10 == 0:
        result = candidate
    
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)