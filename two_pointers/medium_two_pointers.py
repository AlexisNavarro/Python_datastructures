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


    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen =  { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            #check if the current value is a close char
            if c in closeToOpen:
                #if stack is not empty and last item in the stack matches with the current value in the hashmap
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        

    #Find the maximum amount of water that a container can store
    def maxArea(self, heights: List[int]) -> int:

        #initialize 2 pointers, start and end
        l, r = 0, len(heights) - 1
        max_water = 0 

        while l < r:

            #obtain the width and height between the two pointers to get the area
            width = r-l
            height = min(heights[r], heights[l])
            area = width * height

            max_water = max(area, max_water) #obtain the max_water between the current area and the max_water we have currently

            #if the left pointer is smaller than the right then increment the left else the right         
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_water


        

