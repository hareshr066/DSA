class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # here we are using the kadane algorithm !
        maxi=float('-inf')
        curr=0
        for x in nums :
            curr+=x
            maxi=max(maxi,curr)
            if curr<0:
                curr=0
        return maxi