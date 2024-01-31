from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numParent = [0 for _ in range(numCourses)]
        childs = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            numParent[a] += 1
            childs[b].append(a)
        
        visited = []
        for i in range(numCourses):
            if numParent[i] == 0:
                visited.append(i)
        
        cnt = 0
        while visited:
            n = visited.pop()
            cnt += 1
            for c in childs[n]:
                numParent[c] -= 1
                if numParent[c] == 0:
                    visited.append(c)
        
        if cnt == numCourses:
            return True

        return False
        
        