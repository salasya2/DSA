class Solution:
    def trap(self, height: List[int]) -> int:


        res = 0

        n = len(height)
        
        i = 0
        j = n - 1
        k = 0
        l,r = 0, 0
        while i<j:

            l = max(l,height[i])
            r = max(r,height[j])
            
            
            if l < r:
                res +=max(0, min(r,l) - height[i])
                i+=1
            else:
                res +=max(0, min(r,l) - height[j])
                j -=1
            
            
        return res       