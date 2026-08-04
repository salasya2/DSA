class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        i = 0
        j = n - 1
        heightMin = 0
        while i < j:
            
            if height[i] < height[j]:
                heightMin = height[i]
                res = max(res,heightMin * (j - i ))
                i += 1
            else:
                heightMin = height[j]
                res= max(res,heightMin * (j - i ))
                j -= 1
        return res