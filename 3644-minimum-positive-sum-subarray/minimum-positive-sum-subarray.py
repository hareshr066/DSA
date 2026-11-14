class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        if not nums:
            return -1
        mini = float('inf')
        n = len(nums)
        for i in range(n):
            ds = []
            for j in range(i, min(i + r, n)):
                ds.append(nums[j])
                if l <=len(ds) <= r:
                    sumi= sum(ds)
                    if sumi> 0:
                        mini = min(mini, sumi)
        return mini if mini != float('inf') else -1