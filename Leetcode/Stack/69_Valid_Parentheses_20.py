class Solution:
    from typing import List
    def isValid(self, s: str) -> bool:
        st=[] #stack
        for i in range(len(s)):
            if s[i]=='[' or s[i]=='(' or s[i]=='{':
                st.append(s[i])

            if not st:
                return False
            elif s[i]==')'  and st[-1]=='(':
                st.pop()

            elif s[i]==']'  and st[-1]=='[':
                st.pop()

            elif s[i]=='}'  and st[-1]=='{':
                st.pop()
                
        if st:
            return False
        return True