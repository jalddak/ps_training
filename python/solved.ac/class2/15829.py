N = int(input())
cmd = input()

result = 0
for i in range(N):
    result += (ord(cmd[i])-96) * 31 ** i

result %= 1234567891

print(result)