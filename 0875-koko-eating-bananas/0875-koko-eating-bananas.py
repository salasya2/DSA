class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort() 
        l = 1
        r = piles[-1]
        n = len(piles)
        res = 0
        while l <= r:
            m = l + (r - l)//2
            count = 0
            for p in piles:

                count += math.ceil(p/m)
            # print(count)
            if count <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res