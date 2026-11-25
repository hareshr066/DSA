from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t)
        d1 = Counter(s)
        d2 = Counter(t)
        if len(s)!=len(t):
            return False
        for k,v in d1.items():
            if not d2[k] or d1[k] != d2[k]:
                return False
        return True

        