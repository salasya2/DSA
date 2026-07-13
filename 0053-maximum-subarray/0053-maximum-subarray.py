class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        max_so_far = float("-inf")
        max_ending = 0
        
        for num in nums:
            max_ending = max(num,max_ending + num)
            max_so_far = max(max_so_far,max_ending)
        return max_so_far