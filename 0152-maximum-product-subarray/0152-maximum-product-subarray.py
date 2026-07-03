class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curMax,curMin = 1,1
        res = nums[0]

        for  num in nums:

            tmp = curMax * num

            curMax = max(tmp,curMin*num,num)
            curMin = min(tmp,num*curMin,num)
            res = max(curMax,res)
        return res