
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0 , rows-1

        while top <= bottom:
            # Perform binary search to find the potential row
            row = (top+bottom)//2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        #If no valid row is found that could contain the target
        if not (top <= bottom):
            return False

        # Perform binary search within the identified row
        row = (top+bottom) // 2
        l,r = 0, cols-1

        # Binary search for the target in the selected row
        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l=m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
            
        return False


            