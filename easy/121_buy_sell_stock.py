from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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


print(Solution().maxProfit([7,1,5,3,6,4])) # output = 5
print(Solution().maxProfit([7,6,4,3,1])) # output = 0
