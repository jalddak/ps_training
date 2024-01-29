class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        dp = [1]

        for i in range(1, len(s)):
            next = 0
            if int(s[i]) != 0:
                next += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                if i >= 2:
                    next += dp[i-2]
                else:
                    next += 1
            dp.append(next)
            
        return dp[-1]

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        dp = [0 for _ in range(len(s))]
        dp[0] = 1

        for i in range(1, len(s)):
            if int(s[i]) != 0:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                if i >= 2:
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 1

        return dp[-1]

                        