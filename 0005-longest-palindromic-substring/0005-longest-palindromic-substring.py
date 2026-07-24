class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        res = [0,0]
        maxLen = 1
        for i in range(n):
            if n - i + 1 <= maxLen/2:
                break 
            l,h = self.helper(s,i)
            
            if h-l+1 > maxLen:
                maxLen = h - l + 1
                res[0],res[1] = l,h
            
        return s[res[0]:res[1]+1]
        
    def helper(self,s,i):
        
        l = i
        h = i 
        while l > 0 and h < len(s) -1 and s[l - 1] == s[h + 1]:
            l -= 1
            h += 1

        
        indices = [l,h]
        if  i == len(s) -1:
            return indices
        l = i 
        h = i + 1
        if s[l] != s[h]:
            return indices
        while l > 0 and h < len(s) - 1 and s[l-1] == s[h+1]:
            l -= 1
            h += 1

        if h - l  + 1 > indices[1] - indices[0] + 1:
            return [l,h]
        return indices


        