class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix[0])    
        n = len(matrix)

        t = 0
        b = n - 1

        while t <= b:
            
            l  = 0 
            r = m - 1
            mid_row = (t+b)//2
            if target > matrix[mid_row][r]:
                    t = mid_row + 1
            elif target < matrix[mid_row][l]:
                    b = mid_row - 1
            else:
                while l <= r :

                    mid = (l+r)//2

                    if target == matrix[mid_row][mid]:
                        return True
                    elif target > matrix[mid_row][mid]:
                        l = mid+1
                    else:
                        r = mid -  1
                return False

        return False