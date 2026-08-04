class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        '''
         cost[i] -> price of  ith ice cream

         max num of ice cream bars he can buy with coins 

         

        '''
        costs.sort()
        count = {}

        for c in costs:

            count[c] = count.get(c,0) + 1

        res = 0
        for c,count in count.items():
            if c > coins:
                continue
            while count:

                res += 1
                count -= 1
                coins -= c
                if c > coins:
                    return res
        return res




        