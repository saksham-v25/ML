class Solution:
    from typing import List
    def removeDuplicates(self, s: str) -> str:
        stack = []
        res = []

        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue
            elif stack[-1] == s[i]:
                stack.pop()
                continue

            stack.append(s[i])

        while stack:
            res.append(stack.pop())
        res.reverse()
        return "".join(res)
