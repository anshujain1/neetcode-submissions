class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        for i in range(1,len(prices)):
            cost =prices[i] - minBuy
            minBuy = min(minBuy , prices[i])
            maxP = max(maxP , cost)
        return maxP

