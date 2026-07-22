class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        

        n = len(s)
        maxLen = 0
        if n == 0:
            return 0

        seen = {}
        start = 0

        for end, c in enumerate(s):

            if c in seen and seen[c] >= start:
                start = seen[c] + 1
            
            seen[c] = end

            maxLen = max(maxLen, end - start + 1)
        
        return maxLen

        