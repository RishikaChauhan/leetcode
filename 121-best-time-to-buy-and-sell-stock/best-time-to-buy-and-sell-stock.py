class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = j = 0
        p = 0
        for j in range(len(prices)):
            p = max(p, prices[j]-prices[i])
            if prices[j]<prices[i]:
                i=j
        return p