class Solution:
    from typing import List
    def longestPalindrome(self, s: str) -> int:

        n=len(s)

        f={

        }
        
        for i in range(n):
            if s[i] not in f:
                f[s[i]]=1
            else:
                f[s[i]]+=1

        odd=False

        res=0

        for key,value in f.items():
            val=value
            if val%2==0:
                res+=val
            else:
                odd=True
        
        if odd==False:
            return res
    
        for key,value in f.items():
            val=value
            if val%2==1:
                res+=val-1

        return res+1