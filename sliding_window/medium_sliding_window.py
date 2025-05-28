from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):

            #remove the duplicates in the set until there are no more
            #also increment the left pointer by 1 after removal
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            #add the current character to the set to make sure we know we visited that character
            charSet.add(s[r])

            # res will be the max between res and the current index (right pointer) - left pointer + one for inclusive
            res = max(res, r - l + 1)
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        freq = {} #hashmap to count occurences of each char
        res = 0

        l = 0
        maxf = 0 #frequency of the most common character in the current window

        #r is the right pointer
        for r in range(len(s)):
            
            freq[s[r]] = 1 + freq.get(s[r], 0) #count the character at index r
            maxf = max(maxf, freq[s[r]]) #update max frequency

            #check if the window is valid, window size -frequent character count
            #if the amount of characters needed to replace are greater than k then shrink the window from the left
            while (r-l+1) - max(freq.values()) > k: 
                freq[s[l]]-=1
                l += 1

            res = max(res, r-l+1) #store the largest window size
        return res

    #You are given an array prices where prices[i] is the price of a given stock on the ith day.
    #You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    #Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        maxP = 0

        #traverse the list based on the right pointer
        while r < len(prices):
            #if the left pointer value is less than the right pointer value, then calculate the profit and update the maxP
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r #set the left to the lowest value if prices[l] is greater than prices[r]
            r+=1
        return maxP
    
    #You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    #On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
    #Find and return the maximum profit you can achieve.
    def maxProfit2(self, prices: List[int]) -> int:
        l, r = 0, 1

        profits = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                # Accumulate profit when there is an increase in price
                profits += prices[r] - prices[l]
                
                l = r  # Move the left pointer to the right to start from the new base

            else:
                # If the current price is lower or equal, update the left pointer
                l=r 

            r+=1  # Move the right pointer to the next day

        return profits
    
    # Given an array of positive integers nums and a positive integer target
    # return the minimal length of a subarray whose sum is greater than or equal to target.
    # If there is no such subarray, return 0 instead.
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        total = 0
        min_l = float('inf') #set min_l to float to be able to compare properly the sizes of the window

        for r in range(len(nums)):
            total += nums[r]

            #as long as the total is greater than the target, then compare the window sizes and shrink the window once after
            while total >= target:
                min_l = min(min_l, r-l+1) #compare the window sizes and keep the smallest one
                total-=nums[l] #subract the value from the total from the left pointer
                l+=1

        if min_l == float('inf'):
            return 0 #return 0 if there is no valid sub_array
        else:
            return min_l



