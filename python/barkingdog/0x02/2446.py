n = int(input())

answer = []

for i in range(n, 0, -1):
    s = " " * (n - i) + "*" * (i + i - 1)
    answer.append(s)
    print(s)

answer.pop()
while answer:
    print(answer.pop())