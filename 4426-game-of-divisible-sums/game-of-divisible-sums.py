class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n = len(nums)
        f =[0]*(n+2)
        for i in range(n-1,-1,-1):
            best=-float('inf')
            for k in (1,2):
                if i+k <= n:
                    s=sum(nums[i:i+k])
                    best=max(best,s-f[i+k] if s%3==0 else s+f[i+k])
            f[i]=best
        return f[0]
        