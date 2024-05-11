class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i=0
        s=0
        j=0
        while i<len(prices)-1:
            if prices[i+1]>prices[i]:
                b = prices[i]
                for j in range(i, len(prices)-1):
                    # if j==len(prices):s = prices[-1]
                    if prices[j+1]<prices[j]:
                        s = prices[j]
                        break

                    if j==len(prices)-2: s=prices[-1]
                print(b,s)
                i=j+1
                profit+=(s-b)
            else:
                i=i+1
        return profit
            