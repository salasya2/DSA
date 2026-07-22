class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res = ""
        resLen = float("inf")
        start = 0
        freq1 = {}
        freq2 = {}

        for c in t:
            freq1[c] = freq1.get(c,0) + 1
        
        need = len(freq1)
        have = 0
        start = 0
        for end in range(len(s)):

            freq2[s[end]] = freq2.get(s[end],0) + 1

            if s[end] in freq1 and freq1[s[end]] == freq2[s[end]]:
                have += 1
            
            while have == need:

                Len = end - start + 1
                if Len < resLen:
                    res = s[start : end + 1]
                    resLen = Len
                
                freq2[s[start]] -= 1
                if s[start] in freq1 and freq1[s[start]] > freq2[s[start]]:
                    have -= 1
                start += 1
        
        return res




        