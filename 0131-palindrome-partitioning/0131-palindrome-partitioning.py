class Solution:

    def check(self,s):
        i = 0
        j = len(s) - 1

        while i<=j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        substrings = []

        curr = []
        substr = ""
        def dfs(j):
            nonlocal substr
            if j >= len(s):
                res.append(substrings.copy())
                return
            
            for i in range(j,len(s)):


                if self.check(s[j:i+1]):
                    substrings.append(s[j:i+1])
                    dfs(i+1)
                    substrings.pop()
                
        dfs(0)
        
        return res
                