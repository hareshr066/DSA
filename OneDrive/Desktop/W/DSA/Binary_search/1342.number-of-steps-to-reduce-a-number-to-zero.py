#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        def fn(n):
            c+=1
            if n==0:
                return c
            if n%2==0:
                fn(n/2)

            else :
                fn(n-1)

        return fn(num)

# @lc code=end

