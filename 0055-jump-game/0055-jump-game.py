class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        goal = n -1
        for i in range(n-1,-1,-1):

            if i + nums[i] >= goal:
                goal = i
        return (goal == 0)


        #     steps  = nums[i]

        #     for j in range(1,steps+1):

        #         if helper(i + j):
        #             return True
            
            
        
        # if helper(0):
        #     return True
        # return False
        #O(n^N/m) O(n^n/m)