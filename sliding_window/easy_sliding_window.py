from typing import List


class Solution:
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

        