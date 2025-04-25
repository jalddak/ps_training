t = int(input())

answer = []
for c in range(1, t+1):
    num, cnt = map(int, input().split())
    result = ""

    strNum = str(num)
    numLen = len(strNum)
    stack = [strNum]

    for _ in range(cnt):
        nStack = set()
        while stack:
            temp = stack.pop()
            numList = list(temp)
            for i in range(numLen):
                for j in range(i+1, numLen):
                    candidate = list(temp)
                    candidate[i] = numList[j]
                    candidate[j] = numList[i]
                    nStack.add("".join(candidate))
        stack = list(nStack)

    result = sorted(stack, reverse=True)[0]
    answer.append("#" + str(c) + " " + result)


for a in answer:
    print(a)