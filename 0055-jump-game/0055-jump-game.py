class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = [False] * n

        dp[n-1] = True

        for i in range(n-2,-1,-1):

            for j in range(i + 1, min(n,i + nums[i] + 1)):

                if dp[j]:
                    dp[i] = True
        print(dp)
        return dp[0]
        # def helper(i):

        #     if i >= n-1:
        #         return True
        #     if nums[i] == 0:
        #         return False

        #     steps  = nums[i]

        #     for j in range(1,steps+1):

        #         if helper(i + j):
        #             return True
            
            
        
        # if helper(0):
        #     return True
        # return False
        #O(n^N/m) O(n^n/m)