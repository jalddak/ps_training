def solution(num, k):
    answer = 0
    num = str(num)
    for index in range(len(num)):
        if int(num[index]) == k:
            return index + 1
    return -1