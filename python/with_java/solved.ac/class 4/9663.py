n = int(input())
check = [-1 for _ in range(n)]

answer = 0
def solution(depth):
    global answer

    if depth == n:
        answer += 1
        return

    for i in range(n):
        flag = False
        for j in range(depth):
            if check[j] == i or abs(depth - j) == abs(i - check[j]):
                flag = True
                break
        if flag:
            continue
        check[depth] = i
        solution(depth + 1)

solution(0)
print(answer)