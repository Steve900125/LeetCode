from typing import List
# Wrong answer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_val = 0, 1, 0

        while right < len(prices):
            diff = prices[right] - prices[left]
            if diff < 0:
                left += 1
                right = left + 1
            else:
                if diff > max_val:
                    max_val = diff
                right += 1
        
        return max_val