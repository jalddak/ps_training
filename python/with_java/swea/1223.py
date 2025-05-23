tcCnt = 10

def calc(numStack, buho):
    before = buho.pop()
    n1, n2 = numStack.pop(), numStack.pop()
    if before == "+":
        numStack.append(n1 + n2)
    else:
        numStack.append(n1 * n2)

answer = []
for tc in range(1, tcCnt + 1):
    n = int(input())
    s = input()
    numStack = []
    buho = []
    for c in s:
        if c.isdigit():
            numStack.append(int(c))
            continue
        if not buho or (c == "*" and buho[-1] == "+"):
            buho.append(c)
            continue
        calc(numStack, buho)
        buho.append(c)
    
    while buho:
        calc(numStack, buho)
    result = numStack.pop()
    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)

print("\n".join(answer))