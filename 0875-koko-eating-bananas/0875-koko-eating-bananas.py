class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        max_ele = max(piles)


        min_ele = 1

        while min_ele < max_ele :

            mid = (min_ele + max_ele)//2

            res = 0
            
            for p in piles:
                
                res += math.ceil(p/mid)

            if res > h :

                min_ele = mid + 1
            
            else:

                max_ele = mid 

        return max_ele

