# while True:
#     lens = list(map(int, input().split()))
#     lens.sort()
#     if (lens[0] == lens[1] == lens[2] == 0):
#         break
#     if (lens[0] ** 2 + lens[1] ** 2 == lens[2] ** 2):
#         print("right")
#     else:
#         print("wrong")

import sys
input = sys.stdin.readline

while(True):
    cmd = list(map(int, input().split()))
    cmd.sort()
    a, b, c = cmd
    if (a == b == c == 0):
        break
    elif (a*a + b*b == c*c):
        print("right")
    else:
        print("wrong")

