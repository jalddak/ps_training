answer = []

for tc in range(1, 11):
    sb = "#" + str(tc) + " "
    length = int(input())
    board = [list(map(int, input().split())) for _ in range(length)]

    result = 0
    for i in range(length):
        flag = False
        cur = -1
        cnt = 0
        for j in range(length):
            if not flag and board[j][i] in set([0, 2]):
                continue
            flag = True
            if board[j][i] == 0 or cur == board[j][i]:
                continue
            cur = board[j][i]
            if cur == 2:
                cnt += 1
        result += cnt

    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)
            