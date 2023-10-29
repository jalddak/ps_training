N = int(input())
num = 1

for n in range(1, N+1):
    num *= n

num = list(str(num))
num.reverse()

result = 0
for i in range(len(num)):
    if num[i] != '0':
        break
    result += 1

print(result)