class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        i = 0
        j = i + 1
        n = len(prices)

        while i < n and j < n:

            
            if prices[j] < prices[i]:
                i+=1
            else:
                res = max(res,prices[j] - prices[i])
                j += 1

        return res
        