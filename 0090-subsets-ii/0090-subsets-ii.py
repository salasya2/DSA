class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        subsets= []
        
        def dfs(idx):

            res.append(subsets.copy())
            

            for j in range(idx, len(nums)):

                if j > idx and nums[j] == nums[j-1]:
                    continue
                
                subsets.append(nums[j])
                dfs(j+1)
                subsets.pop()
        dfs(0)
        return res
            
            
