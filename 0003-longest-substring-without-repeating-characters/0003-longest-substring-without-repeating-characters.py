class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        start = 0
        res = 0
        d = {}

        for end in range(n):
            c = s[end]
            if c in d and d[c] >= start:
                start = d[c] + 1
            
            d[c] = end

            res=  max(res,end-start + 1)
        return res