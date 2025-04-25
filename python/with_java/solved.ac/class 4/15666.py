n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
n = len(nums)

answer = []
def recursion(depth, result, k):
    if depth == m:
        answer.append(" ".join(map(str, result)))
        return

    for i in range(k, n):
        result.append(nums[i])
        recursion(depth + 1, result, i)
        result.pop()

recursion(0, [], 0)
for a in answer:
    print(a)