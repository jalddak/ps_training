answer = []

n = int(input())

for i in range(1, n + 1):
    s = "*" * i + " " * (2 * (n - i)) + "*" * i
    print(s)
    answer.append(s)

answer.pop()
while answer:
    print(answer.pop())
