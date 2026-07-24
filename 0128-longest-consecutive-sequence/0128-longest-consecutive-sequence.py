class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        
        return length
        O(n)

        
        '''


        d = set(nums)
        res = 0
        
        for num in d:
            
            if num + 1 not in d:
                count =  1
                while num - 1 in d:
                    
                    count += 1
                    num = num - 1
                
                res = max(res , count)
        
        return res


        