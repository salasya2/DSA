class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        n = len(s)

        """
        catsincars
        cats cat sin in car

        cats incars or cat sincars
           incars   or   sin cars
           in cars
        
        """

        dp = [False] * (n+1)

        dp[n] = True
        print(dp)
        for i in range(n-1,-1,-1):

            for word in wordDict:

                if len(word) + i <= n and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                
                if dp[i]:
                    break
            

        return dp[0]
