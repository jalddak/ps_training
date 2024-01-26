from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [""]
        for c in s:
            for i in range(len(dp)):
                dp[i] = dp[i]+c
                if dp[i] in wordDict:
                    dp.append("")
            dp = list(set(dp))
        dp = set(dp)
        if "" in dp:
            return True
        return False
    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n)]
        wordDict = set(wordDict)
        for i in range(n):
            sub = s[:i+1]
            if sub in wordDict:
                dp[i] = True
            else:
                for j in range(i):
                    if dp[j] and s[j+1:i+1] in wordDict:
                        dp[i] = True
        
        return dp[-1]