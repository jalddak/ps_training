tcCnt = 10
answer = []

def solution(tc):
    sb = "#" + str(tc) + " "
    n = int(input())
    codes = list(map(int, input().split()))
    cmdN = int(input())
    cmds = list(input().split("I "))
    for i in range(1, cmdN+1):
        cmd = list(map(int, cmds[i].split()))
        insertIdx = cmd[0]
        cnt = cmd[1]
        for j in range(cnt):
            codes.insert(insertIdx + j, cmd[2 + j])
    sb += " ".join(map(str, codes[:10]))
    return sb



for tc in range(1, tcCnt+1):
    answer.append(solution(tc))

for a in answer:
    print(a)