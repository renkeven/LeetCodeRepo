class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        diff_price = [max(0, prices[i+1] - prices[i]) for i in range(len(prices) - 1)]
        
        return sum(diff_price)