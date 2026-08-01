class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        perm = []
        def helper(i):
            if len(perm) == n:
                res.append(perm[:])
                return
            
            for j in range(n):
                if nums[j] in perm:
                    continue
                perm.append(nums[j])
                helper(j)
                perm.pop()
                
        
        helper(0)
        return res

        