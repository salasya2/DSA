class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.res = []
        self.count = defaultdict(int)
        curr = []
        A = []

        for num in candidates:
            if self.count[num] == 0:
                A.append(num)
            
            self.count[num] += 1
        
        self.backtrack(A,curr,target,0)
        return self.res
    
    def backtrack(self,nums, curr, target, i):

        if target == 0:
            self.res.append(curr.copy())
            return
        if target < 0 or i >= len(nums):
            return 

        if self.count[nums[i]] > 0:
            curr.append(nums[i])
            self.count[nums[i]] -= 1
            self.backtrack(nums,curr, target-nums[i], i)
            self.count[nums[i]] += 1
            curr.pop()
        
        self.backtrack(nums,curr, target, i + 1)
        
        