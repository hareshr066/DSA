from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t)
        d1,d2= dict(),dict()
        for i in s :
            d1[i]=d1.get(i,0)+1
        for i in t :
            d2[i]=d2.get(i,0)+1
        # d1 = Counter(s)
        # d2 = Counter(t)
        if len(s)!=len(t):
            return False
        for k,v in d1.items():
            if d1[k] != d2.get(k,0):
                return False
        return True

        