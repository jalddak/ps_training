from collections import deque

def dfs(nums):
    for i in range(len(nums)):
        nextnums = [nums[i][:len(nums[i])//2], nums[i][len(nums[i])//2+1:]]

        # 가운데가 0이라도 자식 노드에 1이 없으면 0이 와도 된다.
        if nums[i][len(nums[i])//2] != '1':
            for sub in nextnums:
                if '1' in list(sub):
                    return False
        # 자식노드 포함 길이가 3 이하인데 가운데가 1이면 안봐도 통과다
        elif len(nums[i]) <= 3:
            continue
        # 자식노드도 확인해본다.
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
        while 2 ** n - 1 < len(num):
            n += 1
            if 2**n-1 == len(num):
                check = 1
        
        dif = 2**n-1 - len(num)
        # 이 부분에서 나는 뒤에도 0을 게속 추가해준것도 생각하다가 게속 틀렸었는데, 뒤에 0을 추가해버리면 아예 숫자가 달라져서 하면안된다.
        # ex) 4 : 100 = 00100 != 10000 = 16
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