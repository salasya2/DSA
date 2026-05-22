class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        res = [num for num in nums[:k]]
        heapq.heapify(res)

        for num in nums[k:]:

            if num > res[0]:
                heapq.heappop(res)
                heapq.heappush(res,num)
            
        
        return res[0]
        