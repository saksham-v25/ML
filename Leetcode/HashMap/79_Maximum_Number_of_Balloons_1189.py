class Solution:
    from typing import List 
    def maxNumberOfBalloons(self, text: str) -> int:
        n=len(text)
        have={}
        need = {
        'b': 1,
        'a': 1,
        'l': 2,
        'o': 2,
        'n': 1
            }
        res = float('inf')   

        for i in range(n):
            if text[i] not in have:
                have[text[i]]=1
            else:
                have[text[i]]+=1

        for key,value in need.items():
            
            fneed=value
            fhave = have.get(key, 0)

            time = fhave // fneed

            res=min(res,time)
            
        return res

        