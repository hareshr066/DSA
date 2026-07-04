#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        nums.sort()
        def canplace(mid,nums,n,totcow):
            last = nums[0]
            cnt=1
            for i in range (1,n):
                if nums[i]-last >= mid:
                    cnt+=1
                    last=nums[i]
                if cnt>=totcow:
                    return True
            return False
        low,high=1,nums[-1]-nums[0]
        ans=0
        while low<= high:
            mid = (low+high)//2
            bb=canplace(mid,position,len(position),m)
            if bb :
                ans=mid
                low=mid+1
            else :
                high=mid-1
        return ans

# @lc code=end

