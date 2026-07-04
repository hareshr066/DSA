#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums :
            news=[]
            for r in res:
                news.append(r+[num])
            res.extend(news)
        return res
        
# @lc code=end

