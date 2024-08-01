class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # nums.sort()
        # # if nums[1]>=0
        # return nums[-1]*nums[-2] - nums[0]*nums[1]


        a,b,c,d = sorted(nums[:4], reverse = True)

        for n in nums[4:]:
            a,b = max(n,a), max(b, min(n,a))
            c,d = min(c, max(n, d)), min(d, n)

        return a*b-c*d
