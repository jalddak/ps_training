N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = set()

def combination(depth, able, index):
    if depth == M and tuple(able[:]) not in result:
        result.add(tuple(able[:]))
        print(" ".join(map(str, able)))
    else:
        for i in range(index, N):
            able.append(nums[i])
            combination(depth+1, able, i+1)
            able.pop()

combination(0, [], 0)