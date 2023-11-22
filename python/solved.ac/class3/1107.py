import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
M = int(input())
bds = set([])
if M != 0:
    bds = set(input().split())
result = abs(int(N)-100)

def recursion(n, cnt, ud):
    global result
    str_n = str(n)
    flag = True
    for c in str_n:
        if c in bds:
            flag = False
            break
    if flag:
        result = min(result, len(str_n) + cnt)
    
    elif result > cnt:
        if ud == "+":
            recursion(n+1, cnt+1, "+")
        elif ud == "-" and n != 0:
            recursion(n-1, cnt+1, "-")
        elif n != 0:
            recursion(n+1, cnt+1, "+")
            recursion(n-1, cnt+1, "-")
        else:
            recursion(n+1, cnt+1, "+")

recursion(int(N), 0, "")
print(result)