import sys
input = sys.stdin.readline

def count(l, nums):
    cnt = 0
    for num in nums:
        cnt += num // l
    return cnt

def binary_search(nums, n):
    left, right = 1, max(nums)
    while left + 1 < right:
        temp = (left + right) // 2
        cnt = count(temp, nums)
        if cnt >= n:
            left = temp
        else:
            right = temp - 1

    return left, right


def main():
    k, n = map(int, input().split())
    nums = [int(input()) for _ in range(k)]
    l, r = binary_search(nums, n)
    if count(r, nums) >= n:
        print(r)
    else:
        print(l)

if __name__ == "__main__":
    main()