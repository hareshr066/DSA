class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        look = []
        maxi = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in look:
                look.append(s[j])
                maxi = max(maxi, j - i + 1)
                j += 1
            else:
                look.remove(s[i])
                i += 1
        return maxi