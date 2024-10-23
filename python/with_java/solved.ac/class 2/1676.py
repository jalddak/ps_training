n = int(input())
num = 1
for i in range(1, n+1):
    num *= i

num = list(str(num))
num.reverse()

for cnt in range(len(num)):
    if num[cnt] != '0':
        print(cnt)
        break