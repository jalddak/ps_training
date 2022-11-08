def solution(numlist, n):
    answer = []
    numlist.sort()
    numlist.sort(key=lambda x: abs(x-n))
    for index in range(len(numlist) - 1):
        if abs(numlist[index] - n) == abs(numlist[index + 1] - n):
            num = numlist.pop(index)
            numlist.insert(index+1, num)
    answer = numlist
    return answer