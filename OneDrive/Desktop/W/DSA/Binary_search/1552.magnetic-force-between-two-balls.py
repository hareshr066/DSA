#
# @lc app=leetcode id=1552 lang=python3
#
# [1552] Magnetic Force Between Two Balls
#

# @lc code=start
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
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
        low,high=1,position[-1]-position[0]
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

