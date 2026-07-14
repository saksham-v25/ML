class Solution:
    from typing import List
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        stack=[]
        res[n-1]=0
        stack.append(n-1)

        for i in range(n-2,-1,-1):

            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if not stack:
                res[i]=0
            else:
                res[i]=stack[-1]-i
            stack.append(i)
        return res

        