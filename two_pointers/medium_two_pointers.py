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

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        #i is the index, a is the current number
        for i, a in enumerate(nums):
            if i >0 and a == nums[i - 1]:
                continue

            l, r = i+1, len(nums) -1

            while l<r:
                total = a + nums[l] + nums[r]

                if total > 0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])

                    l+=1

                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return res


            
        

