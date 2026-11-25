from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res =[]
        d = defaultdict(list)
        for i in strs :
            key = "".join(sorted(i))
           
            d[key].append(i)
        for k,v in d.items():
            res.append(v)
        return res 
        