class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini = min(nums)
        res = 0
        for x in nums:
            res+=(x-mini)
        return res
        