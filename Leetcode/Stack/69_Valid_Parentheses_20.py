class Solution:
    from typing import List
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):

            if s[i] == "[" or s[i] == "(" or s[i] == "{":
                st.append(s[i])

            else:
                if not st:
                    return False

                elif s[i] == ")":
                    if st[-1] == "(":
                        st.pop()
                    else:
                        return False

                elif s[i] == "]":
                    if st[-1] == "[":
                        st.pop()
                    else:
                        return False

                elif s[i] == "}":
                    if st[-1] == "{":
                        st.pop()
                    else:
                        return False

        if st:
            return False

        return True