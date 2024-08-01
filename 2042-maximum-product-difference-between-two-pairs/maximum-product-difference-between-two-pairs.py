class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        # if nums[1]>=0
        return nums[-1]*nums[-2] - nums[0]*nums[1]

