#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        def fn(n):

            if n==0:
                return 0
            if n==1:
                return 1
            return fn(n-1)+fn(n-2)
        return fn(n)



# @lc code=end

