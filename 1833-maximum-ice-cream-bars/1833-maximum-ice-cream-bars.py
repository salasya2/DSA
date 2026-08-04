class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        '''
         cost[i] -> price of  ith ice cream

         max num of ice cream bars he can buy with coins 

         

        '''
        
        cost_min = cost_max = max(costs)

        freq = [0] * (cost_max + 1)

        for c in costs:
            freq[c] += 1
            cost_min = min(cost_min,c)
        
        res = 0
        for i in range(cost_min, len(freq)):

            f = freq[i]

            if f == 0:
                continue
            buy = min(coins//i,f)
            if buy == 0:
                break
            res += buy
            coins -= buy * i
        return res




        