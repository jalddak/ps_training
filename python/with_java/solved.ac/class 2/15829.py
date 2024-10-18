l = int(input())
cmd = input()

answer = 0
for i in range(l):
    n = ord(cmd[i]) - 96
    answer += n * (31 ** i) % 1234567891
answer %= 1234567891
print(answer)
    