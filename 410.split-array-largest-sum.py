#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(mid,nums,k):
            par=1
            currsum=0
            for i in nums:
                if currsum+i>mid:
                    par+=1
                    currsum=i
                else :
                    currsum+=i
            return par<=k 
        low, high= max(nums),sum(nums)
        ans=high
        while low<= high:
            mid =(low+high)//2
            bb=cansplit(mid,nums,k)
            if bb:
                ans=mid
                high=mid-1
            else :
                low=mid+1
        return ans 

        
# @lc code=end

