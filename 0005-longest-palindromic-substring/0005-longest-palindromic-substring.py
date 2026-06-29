class Solution:


    def helper(self, s):
        n = len(s)
        max_len = -1
        max_substr = ""
        for i in range(n):
            l,h= i,i       
            if max_len == -1:
                max_substr = s[i]
                max_len = 1
            
            while l>=0 and h<=n-1 and s[l] == s[h]:
                l-=1
                h+=1
            substring = s[l+1:h]
            if len(substring) > max_len:
                max_substr = substring
                max_len = len(substring)
        for i in range(n-1):

            l = i 
            h = i + 1
            if max_len == -1:
                max_substr = s[i]
                max_len = 1
            while l>=0 and h<=n-1 and s[l] == s[h]:
                l-=1
                h+=1
            substring = s[l+1:h]
            if len(substring) > max_len:
                max_substr = substring
                max_len = len(substring)
        return max_substr
        return max_substr

    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 0:
            return ""

        
        return self.helper(s)


        