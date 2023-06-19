from collections import deque

def dfs(nums):
    for i in range(len(nums)):
        nextnums = [nums[i][:len(nums[i])//2], nums[i][len(nums[i])//2+1:]]
    
        if nums[i][len(nums[i])//2] != '1':
            for sub in nextnums:
                if '1' in list(sub):
                    return False
        elif len(nums[i]) <= 3:
            continue
        else:
            result = dfs(nextnums)
            if result == False:
                return False
    return True


def solution(numbers):
    answer = []
    binarys = []

    for i in range(len(numbers)):
        binarys.append(bin(numbers[i])[2:])
    for num in binarys:
        n = 0
        check = 0
        candidates = []
        while 2 ** n - 1 < len(num):
            n += 1
            if 2**n-1 == len(num):
                check = 1
        
        dif = 2**n-1 - len(num)
        if check == 0:
            c = deque(list(num))
            for i in range(dif):
                c.appendleft('0')
            num = ''
            for j in range(len(c)):
                num += c[j]
        result = 0
        if num[len(num)//2] != '0':
            if dfs([num]):
                result = 1
        answer.append(result)
        
    return answer