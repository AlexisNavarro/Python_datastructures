from typing import List


class Solution:

    #solving twoSum with two pointers while having space complexity of O(1)
    #our input is a sorted list and we are to return 1-indexed array
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]

            #if our current values are bigger than the target then decrement the right pointer, else increment the left pointer 
            if numbers[l] + numbers[r] > target:
                r-=1
            else:
                l+=1

