class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        res = []

        perm = []


        def helper(i):

            if i==n-1:
                res.append(perm[:])
                return
            

            if i > n:
                return
            
            for j in range(0,n):
                if nums[j] in perm:
                    continue
                perm.append(nums[j])

                helper(i + 1)

                perm.pop()
        helper(-1)
        return res
        