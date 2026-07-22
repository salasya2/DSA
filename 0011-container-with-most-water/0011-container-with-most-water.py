class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)

        if n == 0:
            return 0

        res = 0

        i , j = 0, n - 1

        while i < j:

            res = max((j - i ) * min(height[i],height[j]),res)

            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return res
        