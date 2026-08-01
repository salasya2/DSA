class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)

        # list of unique combinations
        # same number can be chosen many times
        # any two combinations must not be same.

        res = []
        comb = []
        visited = set()
        def helper(i , target):
            if target < 0:
                return 
            if target == 0:
                
                if tuple(sorted(comb)) in visited:
                    return
                res.append(comb[:])
                visited.add(tuple(sorted(comb)))
                return

            for j in range(len(nums)):
                # print(i,nums[j])
                comb.append(nums[j])
                helper(i + 1, target - nums[j])
                comb.pop()
        
        helper(0,target)
        return res
