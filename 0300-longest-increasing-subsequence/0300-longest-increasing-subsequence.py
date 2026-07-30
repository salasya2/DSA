class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1
        n = len(nums)
        dp = [1] * len(nums)


        for i in range(1,len(nums)):

            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    

        return max(dp)
   


  #2^n and O(n)