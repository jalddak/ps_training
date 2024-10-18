# import sys
# input = sys.stdin.readline


# def calc(temp):
#     s_temp = str(temp)
#     result = temp
#     for t in s_temp:
#         result += int(t)
#     return result

# def main():
#     n = int(input())
#     sn = str(n)
#     cnt = (len(sn)-1) * 9 + int(sn[0])-1
#     temp = n
#     answer = 0
#     while cnt > 0:
#         temp -= 1
#         result = calc(temp)
#         if n == result:
#             answer = temp
#         cnt -= 1
#     print(answer)
#     return answer

# if __name__ == '__main__':
#     main()

strNum = input()
num = int(strNum)
length = len(strNum)

flag = False
for n in range(num - length*9, num):
    if n < 0: continue
    candidate = n + sum(map(int, list(str(n))))
    if candidate == num:
        print(n)
        flag = True
        break
if not flag:
    print(0)