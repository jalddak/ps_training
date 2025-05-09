tcCnt = 10

buhoSet = set(["(", ")", "+", "*"])

answer = []
for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    
    length = int(input())
    cmd = input()

    buho = []
    nums = []


    for c in cmd:
        if c in buhoSet:
            buho.append(c)
            if buho[-1] == ")":
                buho.pop()
                num = nums.pop()
                while buho:
                    cur = buho.pop()
                    if cur == "(":
                        break
                    num += nums.pop()
                if buho and buho[-1] == "*":
                    buho.pop()
                    num *= nums.pop()
                nums.append(num)
        else:
            num = int(c)
            if buho and buho[-1] == "*":
                buho.pop()
                num *= nums.pop()
            nums.append(num)
    
    sb += str(nums.pop())
    answer.append(sb)

for a in answer:
    print(a)
        


