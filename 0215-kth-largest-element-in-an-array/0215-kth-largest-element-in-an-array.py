class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)

        heapq.heapify(nums) #nlogn

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]
        