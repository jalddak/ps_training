answer = []

n = int(input())
for i in range(1, n + 1):
    s = " " * (n - i) + "*" * (i + i - 1)
    print(s)
    answer.append(s)

answer.pop()
while answer:
    print(answer.pop())