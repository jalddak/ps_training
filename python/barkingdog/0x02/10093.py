a, b = map(int, input().split())

if a > b:
    temp = a
    a = b
    b = temp

answer = [n for n in range(a + 1, b)]
cnt = len(answer)
print(cnt)
print(*answer)