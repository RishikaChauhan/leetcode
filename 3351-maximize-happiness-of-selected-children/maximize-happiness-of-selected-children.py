class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        h=0
        happiness = sorted(happiness)
        for i in range(k):
            happy = happiness[-1*i-1]
            if happy-i>=0:
                h += happy-i
                happiness[-1*i-1]=0
            # for j in range(len(happiness)):
            #     happiness[j]=happiness[j]-1
                
                
            # print(happiness)
        return h
        # h = sorted(happiness, reverse = True)
        # ans = 0
        # for i in range(k):
        #     if h[i]-i>=0:
        #         ans += h[i]-i
        #     else:
        #         return ans
        # return ans