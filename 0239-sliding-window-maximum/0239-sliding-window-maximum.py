from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []

        
        d = deque([])
        

        for i in range(len(nums)):
            

            while len(d) > 0 and nums[d[-1]] <= nums[i]:

                    d.pop()

            d.append(i)

                

            if d[0] <= i - k:

                d.popleft()
            
            # print(d)
            if i> k-2:
                res.append(nums[d[0]])
            

        return res



        