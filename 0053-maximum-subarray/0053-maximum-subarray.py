class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_max = nums[0]
        global_max = nums[0]

        for num in nums[1:]:

            curr_max = max(num,curr_max+num)
            global_max = max(global_max,curr_max)
        
        return global_max