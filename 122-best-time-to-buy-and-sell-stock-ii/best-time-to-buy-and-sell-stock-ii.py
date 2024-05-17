class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                b= prices[i]
                j=i+1
                # while prices[j]>prices[i]:
                    # j+=1
                ret += prices[j]-prices[i]
        return ret