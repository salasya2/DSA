class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        count = defaultdict(int)
        subset = []

        for num in nums:
            count[num] += 1
        mask = 0
        def dfs(subset,mask):

            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if not (mask&(1<<i)):
                    
                    subset.append(nums[i])
                    dfs(subset,(mask|(1<<i)))
                    subset.pop()
        
        dfs(subset,mask)
        return res