class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        if n > 0 and s[0] == '0':
            return 0
        dp = [0] * (n+1)
        dp[n] = 1

        for i in range(n-1,-1,-1):
            if i == n:
                return 1
            if s[i] == '0':
                dp[i] = 0
                continue
            dp[i] += dp[i+1]
            if i < n - 1:
                if (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                    dp[i] += dp[i+2]
        
        return dp[0]
