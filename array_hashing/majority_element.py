from typing import List


class Solution:

    #problem
    #Given an array nums of size n, return the majority element.
    #The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
    def majorityElement(self, nums: List[int]) -> int:
        mapping = {} #create a hash map to store the number of occurences a value appeared

        #count occurences
        for val in nums:
            if val not in mapping:
                mapping[val] = 1
            else:
                mapping[val] +=1
        
        #check if the value for a number is greater than n/2 times that it appeared
        for key, value in mapping.items():
            if value > len(nums)/2:
                return key