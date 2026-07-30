class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1

        if n == 2:
            return 2
        # dp = [0] * n
        # dp[0] = 1 
        # dp[1] = 2
        # for i in range(2,n):
        #     dp[i] = dp[i-1]+dp[i-2]

        one = 1
        two = 2

        for i in range(2,n):
            temp = one  
            one = two
            two = temp + two
        return two

        #O(n),O(n)