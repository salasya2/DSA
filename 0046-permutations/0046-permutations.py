class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        count = defaultdict(int)
        subset = []

        for num in nums:
            count[num] += 1

        def dfs(subset):

            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if count[nums[i]] > 0:
                    count[nums[i]] -= 1
                    subset.append(nums[i])
                    dfs(subset)
                    count[nums[i]] += 1
                    subset.pop()
        
        dfs(subset)
        return res