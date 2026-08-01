class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)

        # list of unique combinations
        # same number can be chosen many times
        # any two combinations must not be same.

        res = []
        comb = []
        visited = set()
        nums.sort()
        def helper(i , target):
            
            if target == 0:
                res.append(comb[:])
                return

            for j in range(i,len(nums)):
                if nums[j] > target:
                    return 
                comb.append(nums[j])
                helper(j, target - nums[j])
                comb.pop()
        
        helper(0,target)
        return res

        #O()
