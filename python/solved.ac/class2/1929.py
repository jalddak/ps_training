# M, N = map(int, input().split())

# for n in range(M, N+1):
#     check = 0
#     for i in range(2, int(n**(1/2))+1):
#         if n % i == 0:
#             check = 1
#             break
#     if n != 1 and check == 0:
#         print(n)

# 위에가 내코드 아래는 다른 사람코드 약간 변형한거.
# 속도가 압도적으로 빨라서 찾아봄.
n, m = map(int, input().split())
checked = [0 for _ in range(m+1)]
x = 2

checked[1] = 1
for i in range(x, m + 1):
    if i > 1 and checked[i] == 0:
        for j in range(i + i, m + 1, i):
            checked[j] = 1

for i in range(n, m + 1):
    if checked[i] == 0:
        print(i)