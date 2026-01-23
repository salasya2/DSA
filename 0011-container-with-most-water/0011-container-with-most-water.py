class Solution:
    def maxArea(self, heights: List[int]) -> int:

        water = -1

        n = len(heights)
        
        i = 0
        j = n - 1

        while(i < j):

            water = max(water, abs((j-i))*min(heights[i],heights[j]))

            if heights[i] < heights[j]:
                i+=1

            else :
                j-=1


        return water

        