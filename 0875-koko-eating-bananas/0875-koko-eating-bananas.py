class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        '''
        
        h - > no of hours to complete the  bananas
        piles[i] -> no of bananas per pile

        if piles[i] > k then it should take more than 1 hr
        if piles[i] <= k -> 1 hour

        max of k will be < max of piles
        min of k will be let's say 0

        '''
        
        r = max(piles)
        l = 1

        n = len(piles)
        
        while l <= r:

            mid = l + (r - l)//2

            time_taken = 0
            for p in piles:

                time_taken += (p + mid - 1)//mid
                
            if time_taken <= h:
                r = mid - 1
            else:
                l = mid + 1
            
        return l



        