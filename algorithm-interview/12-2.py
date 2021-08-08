import sys

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices)<2:
            return 0
        
        diff = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price, price)
            diff = max(diff, price - min_price)
        
        return diff