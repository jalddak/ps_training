def usingSet(n, nums, m, checked):
    nums = set(nums)
    result = []
    for c in checked:
        if c not in nums:
            result.append(0)
        else:
            result.append(1)

    print(" ".join(map(str, result)))


def binarySearch(nums, target):
    s = 0
    e = len(nums)
    while s + 1 < e:
        mid = (s+e)//2
        if nums[mid] <= target:
            s = mid
        else:
            e = mid
    if nums[s] != target:
        return 0
    else:
        return 1


def usingBinarySearch(n, nums, m, checked):
    nums.sort()
    result = []
    for c in checked:
        result.append(binarySearch(nums, c))
    print(" ".join(map(str, result)))
    

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    checked = list(map(int, input().split()))
    # usingSet(n, nums, m, checked)
    usingBinarySearch(n, nums, m, checked)

if __name__ == "__main__":
    main()