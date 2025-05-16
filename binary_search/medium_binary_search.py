
import math
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

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles [i] number of bananas in the ith pile
        #h represents number of hours to eat the bananas

        max_bananas = 0

        # Find the maximum number of bananas in a single pile
        # (can be replaced with max(piles) for brevity)
        for i in range(len(piles)):
            max_bananas = max(max_bananas, piles[i])
        
        l, r = 1, max_bananas
        res = r

        # Perform binary search between 1 and the largest pile
        while l <= r:
            k = (l+r) // 2 #k is the middle pointer in the array
            hours = 0

            for p in piles:
                #will round out the output
                hours += math.ceil(p/k)

            if hours <= h:
                res = min(res, k)
                r = k - 1 # Update result with a possible smaller speed since we want the min output
            else:
                l = k + 1 # Too slow, need to increase speed
        return res


        