class Solution:
    def rob(self, nums: List[int]) -> int:
        

        '''
         - arranged in circle, so I can only rob one of the edges

            2 , 3, 2 
            s , N , N

            2 , 3, 2
            N,  N , s

            2, 3, 2
            N, s , s

            1 , 2, 3 , 1, 4
            N   s  n   n  S = > 6
            N   n  s   n  s
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return  max(nums[0],nums[1])
        return max(self.helper(nums,1,n),self.helper(nums,0,n-1))
        

    def helper(self, nums, start,end):

        
        one = nums[start]
        two = max(nums[start + 1],nums[start])

        for i in range(start + 2, end):

            temp = two
            two = max(one + nums[i], two)
            one = temp

        return two
