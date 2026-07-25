class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        '''
        -> minimum in rotated sorted array
        -> must resturn the min element
        -> o(logn)
        -> unique elements
        
        '''
        n = len(nums)
        if n == 1:
            return nums[0]

        #7  1  2  3 4 5
        l = 0
        h = n - 1

        while l < h:
            m = l + (h - l)//2
            if nums[h] > nums[m]:
                h = m 
            else:
                l = m + 1

        return nums[l]


        



