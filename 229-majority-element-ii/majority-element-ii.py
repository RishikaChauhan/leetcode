class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = len(nums)//3
        d = {}
        for i in nums:
            d[i] = 1+ d.get(i,0)
        print(d)
        p = []
        for k, v in d.items():
            print(m,v)
            if v>m:

                p.append(k)
        return p