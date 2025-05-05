from typing import List


class Solution:
    #solving the maximum profit you can make by buying stock on one day and selling stock another
    #You can't go back in time to buy or sell stock, you can only move forward
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left = buy right = sell
        max_profit = 0

        while r < len(prices):
            #check if you can make a profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit,profit)
            else:
                l = r #move the left pointer to the new min
            r+=1

        return max_profit

        