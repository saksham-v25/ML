class Solution:
    def findCeil(self, arr, x):
        # code here
        n=len(arr)
        low=0
        high=n-1
        res=-1

        while low <= high:
            guess=(low+high)//2
           
            if arr[guess] < x:
                low=guess + 1
            else: #nums[guess] > target
                res=guess
                high=guess-1

        return res 