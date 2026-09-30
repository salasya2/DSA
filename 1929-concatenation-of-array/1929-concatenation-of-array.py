class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        
        '''
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        '''
        nums.extend( nums)
        return nums