class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        
        for i in spells:
            l = 0
            r = len(potions)-1
            while l<=r:
                m = (l+r)//2
                if potions[m]*i>= success:
                    r = m-1
                else:
                    l= m+1
            # if l<len(potions):

            res.append(len(potions)-l)
            # else:
            #     res.append(0)
        return res

        # for i in spells:
        #     count = 0
        #     for j in potions:
        #         if i*j>=success:
        #             count +=1
        #     res.append(count)
        # return res