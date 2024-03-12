def calc(n, k, ftr, nums, result, visited):
    if n == 0:
        return result
    section = ftr[n] // n
    index, k = k//section, k%section
    temp = 0
    for i in range(len(nums)):
        if visited[i]:
            continue
        if temp == index:
            visited[i] = True
            result.append(nums[i])
            break
        temp += 1
        
    return calc(n-1, k, ftr, nums, result, visited)
        

def solution(n, k):
    ftr = [1, 1]
    for i in range(2, n+1):
        ftr.append(ftr[-1]*i)
    nums = [i for i in range(1, n+1)]
    
    answer = calc(n, k-1, ftr, nums, [], [False for i in range(n)])
    
    return answer

# 효율성 3번 시간초과
def calc(n, k, ftr, nums, result):
    if n == 0:
        return result
    section = ftr[n] // n
    index, k = k//section, k%section
    result.append(nums.pop(index))
    return calc(n-1, k, ftr, nums, result)
        

def solution(n, k):
    ftr = [1, 1]
    for i in range(2, n+1):
        ftr.append(ftr[-1]*i)
    nums = [i for i in range(1, n+1)]
    
    answer = calc(n, k-1, ftr, nums, [])
    
    return answer

# 시간초과
def permutation(depth, n, k, cnt, nums, visited):
    if depth == n:
        cnt += 1
        return nums, cnt
    for i in range(1, n+1):
        if visited[i] == True:
            continue
        nums.append(i)
        visited[i] = True
        nums, cnt = permutation(depth+1, n, k, cnt, nums, visited)
        if cnt == k:
            return nums, cnt
        visited[i] = False
        nums.pop()
    return nums, cnt

def solution(n, k):
    visited = [False for _ in range(n+1)]
    answer, cnt = permutation(0, n, k, 0, [], visited)
    
    
    return answer