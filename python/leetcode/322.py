from collections import deque
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        visited = set(coins)
        queue = deque([[n, 1] for n in coins])
        while queue:
            expSum, cnt = queue.popleft()
            if expSum == amount:
                return cnt
            for n in coins:
                if expSum + n <= amount and expSum + n not in visited:
                    queue.append([expSum + n, cnt + 1])
                    visited.add(expSum + n)
        
        return -1