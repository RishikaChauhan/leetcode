class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common()[0][0]
        # d = {}
        # for i in nums:
        #     d[i] = d.get(i,0)+1
        # mx = [0,0]
        # for k,v in d.items():
        #     if v>mx[1]:
        #         mx = [k,v]
        #     print(mx)
        # return mx[0]