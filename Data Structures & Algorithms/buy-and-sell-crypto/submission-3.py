class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 0
    
        maxprofit = 0
        minbuy = float("inf")

        while right < len(prices):
            maxprofit = max(maxprofit , prices[right]- minbuy)
            minbuy = min(minbuy , prices[right])
            right += 1
        return maxprofit
       