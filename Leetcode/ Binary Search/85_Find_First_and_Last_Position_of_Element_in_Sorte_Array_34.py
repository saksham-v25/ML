class Solution:
    from typing import List
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def lessTarget(nums, target):
            low = 0
            high = n - 1
            res = -1

            while low <= high:

                guess = (low + high) // 2
                if nums[guess] < target:
                    low = guess + 1

                elif nums[guess] > target:
                    high = guess - 1

                else:
                    res = guess
                    high = guess - 1

            return res

        def moreTarget(nums, target):
            low = 0
            high = n - 1
            res = -1

            while low <= high:

                guess = (low + high) // 2
                if nums[guess] < target:
                    low = guess + 1

                elif nums[guess] > target:
                    high = guess - 1

                else:
                    res = guess
                    low = guess + 1

            return res

        first = lessTarget(nums, target)
        last = moreTarget(nums, target)

        return [first, last]
