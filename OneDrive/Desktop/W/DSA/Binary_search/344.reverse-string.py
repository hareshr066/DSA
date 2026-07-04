#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # we can also do this using the two pointer approach of recurrsion
        def f(i,n,s):
            if i>=n//2:
                return
            s[i],s[n-i-1]=s[n-i-1],s[i]
            f(i+1,n,s)
        f(0,len(s),s)

        """
        Do not return anything, modify s in-place instead.
        """
        
# @lc code=end

