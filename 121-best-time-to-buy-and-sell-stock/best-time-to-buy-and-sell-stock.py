class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        profit= 0
        for p in prices[1:]:
            if b>p:
                b = p
            profit = max(profit, p-b)
        return profit