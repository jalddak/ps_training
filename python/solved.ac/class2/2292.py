N = int(input())

result = 1
N -= 1
while N > 0:
    result += 1
    N -= 6 * (result - 1)

print(result)