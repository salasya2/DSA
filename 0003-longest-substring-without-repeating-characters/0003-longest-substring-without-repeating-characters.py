class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        if len(s) < 1:

            return res
        
        prev = 0

        t = []

        for i in range(len(s)):
            
           
            while s[i] in t:

                t.remove(s[prev]) 
                prev+=1

            t.append(s[i])
            res  = max(res,i-prev+1)
            

        return res                
                
            