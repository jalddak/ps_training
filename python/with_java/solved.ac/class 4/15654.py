n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def recursion(depth, result, s):
    if depth == m:
        print(" ".join(map(str, result)))
        return
    
    for i in range(n):
        if i in s:
            continue
        s.add(i)
        result.append(nums[i])
        recursion(depth + 1, result, s)
        result.pop()
        s.remove(i)

recursion(0, [], set())