def main():
    T = int(input())

    nums = []
    for _ in range(T):
        nums.append(int(input()))

    dp = [[1, 0], [0, 1]]

    for i in range(2, max(nums)+1):
        dp.append([dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]])

    for n in nums:
        print(dp[n][0], end = ' ')
        print(dp[n][1])

if __name__ == '__main__':
    main()