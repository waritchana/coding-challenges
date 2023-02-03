from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        day_buy = 0
        day_sell = 1
        max_profit = 0

        while day_sell < len(prices):
            if prices[day_sell] > prices[day_buy]:
                new_profit = prices[day_sell] - prices[day_buy]
                max_profit = max(new_profit, max_profit)
            else:
                day_buy = day_sell
            day_sell += 1
        return max_profit
        """
        # Acts as an unbounded upper value to find minimum value
        # when doing comparison
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


Solution().maxProfit([7,1,5,3,6,4]) # output = 5
Solution().maxProfit([7,6,4,3,1]) # output = 0
