class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        if len(s) < 1:

            return res
        
        prev = 0

        t = [s[prev]]

        for i in range(1,len(s)):

            if s[i] in t:

                res = max(res,len(t))

                if s[i] != s[prev]:
                    
                    while s[i] in t:
                        t.remove(s[prev]) 
                        prev+=1

                    t.append(s[i])
                    # print(t)
                else:
                    prev += 1

            else:

                t.append(s[i])

        res  = max(res,len(t))
        return res                
                
            