class Solution:
    from typing import List
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need={}
        have={}

        def fun(have, need):
            
            for key,value in need.items():

                fneed=value
                fhave = have.get(key, 0)

                if fhave < fneed:
                    return False
            return True 

        for i in range(len(ransomNote)):
            if ransomNote[i] not in need:
                need[ransomNote[i]]=1
            else:
                need[ransomNote[i]]+=1

        for i in range(len(magazine)):
            if magazine[i] not in have:
                have[magazine[i]]=1
            else:
                have[magazine[i]]+=1

        return fun(have, need)
        

        