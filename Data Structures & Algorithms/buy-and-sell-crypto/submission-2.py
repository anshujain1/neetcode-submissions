class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        profit = 0
        for i in prices:
            if min_price > i:
                min_price = i
            profit = i - min_price

            if max_profit < profit:
                max_profit = profit

        return max_profit
