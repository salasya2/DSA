class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        min_price = float("inf")

        res = 0 


        for price in prices:

            min_price = min(price,min_price)

            res  = max(res, price-min_price)
        
        


        return res

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
        