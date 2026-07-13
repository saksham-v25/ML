class Solution:
    from typing import List
    def removeDuplicates(self, s: str, k: int) -> str:
        n=len(s)
        stack=[]

        for i in range(n):

            c=s[i]

            if not stack:
                stack.append([c,1])
                continue
            
            if stack[-1][0] != c:
                stack.append([c,1])
                continue

            if stack[-1][1] < (k-1):
               stack[-1][1] += 1
               continue

            stack.pop()

       
        res = ""

        for ch, count in stack:
            res += ch * count

        return res    
        
        