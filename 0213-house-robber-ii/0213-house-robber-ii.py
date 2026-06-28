class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]
        
        return max(self.helper(nums[0:n-1]),self.helper(nums[1:n]))
    
    def helper(self, nums):

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        rob1 = 0
        rob2 = 0

        for num in nums:
            temp = max(num+rob1,rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
