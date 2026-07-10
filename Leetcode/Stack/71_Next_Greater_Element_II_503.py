class Solution:
    from typing import List 
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        res[n-1]=-1
        stack=[]

        for i in range(2*n-1,-1,-1):

            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            
            if not stack: # matlab stack khaali hai 
                res[i%n]=-1
            else:
                res[i%n]=stack[-1]
            
            stack.append(nums[i%n])

        return res
        