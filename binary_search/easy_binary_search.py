from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:

            #get the middle point by adding adding left to the result of right - left, divided by 2
            # (l + r) // 2 can lead to overflow
            mid = l + ((r - l) // 2)  

            #decrement if current mid is bigger than target, or increment if its less than target
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid]< target:
                l = mid + 1
            else:
                return mid

        return -1
        