class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        coins.sort()
        if amount == 0:
            return 0
        dp[0] = 0
        if amount < coins[0]:
            return -1
        
        for i in range(1, amount + 1):
            if  i < coins[0]:
                
                continue

            for coin in coins:
                if coin > i:
                    continue
                if dp[i - coin] == float("inf"):
                    continue
                else:
                    dp[i] = min(dp[i],1 + dp[i-coin])

        return dp[amount] if dp[amount] != float("inf") else -1

    