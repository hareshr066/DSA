from collections import Counter
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = Counter(nums)
        for k,v in d.items():
            if v>1:
                return True 
        return False
        