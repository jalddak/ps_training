def main():
    T = int(input())
    nums = []
    for _ in range(T):
        nums.append(int(input()))
    
    dp = [0, 1, 2, 4]
    for i in range(4, max(nums)+1):
        dp.append(dp[i-3] + dp[i-2] + dp[i-1])
    
    for n in nums:
        print(dp[n])

if __name__ == '__main__':
    main()