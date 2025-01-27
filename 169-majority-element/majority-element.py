class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i in (nums):
            d[i] = 1 + d.get(i, 0)
        print(d)
        mx = [0,0]
        for i, v in d.items():
            if v>mx[1]:
                mx = [i,v]
        return mx[0]