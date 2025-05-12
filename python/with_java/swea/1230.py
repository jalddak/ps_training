# import sys
# sys.stdin = open('./python/with_java/swea/input.txt', 'r')
# sys.stdout = open('./python/with_java/swea/output.txt', 'w')

tcCnt = 10

answer = []
for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    n = int(input())
    nums = list(map(int, input().split()))
    cmdN = int(input())
    cmds = input().split()
    i = 0
    temp = 0
    while temp < cmdN:
        if cmds[i] == "I":
            i += 1
            x = int(cmds[i])
            i += 1
            y = int(cmds[i])
            for d in range(y):
                i += 1
                nums.insert(x+d, cmds[i])
        elif cmds[i] == "D":
            i += 1
            x = int(cmds[i])
            i += 1
            y = int(cmds[i])
            del nums[x:x+y]
        elif cmds[i] == "A":
            i += 1
            y = int(cmds[i])
            for _ in range(y):
                i += 1
                nums.append(int(cmds[i]))
        i += 1
        temp += 1

    result = nums[:10]
    for r in result:
        sb += str(r) + " "
    answer.append(sb)

for a in answer:
    print(a)