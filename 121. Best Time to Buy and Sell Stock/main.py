from typing import List
# bad solution Time Over
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0

        for i in reversed(range(len(prices))):
            for j in reversed(i):
                if prices[i] - prices[j] >= max_value:
                    max_value = prices[i] - prices[j]
        
        return max_value
            