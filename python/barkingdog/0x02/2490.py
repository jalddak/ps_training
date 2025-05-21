for _ in range(3):
    cnt = 0
    nums = list(map(int, input().split()))
    answer = "E"
    for n in nums:
        if n == 0:
            cnt += 1
    if cnt == 1:
        answer = "A"
    elif cnt == 2:
        answer = "B"
    elif cnt == 3:
        answer = "C"
    elif cnt == 4:
        answer = "D"
    print(answer)