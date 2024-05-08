class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r = nums.count(0)
        w = nums.count(1)
        b = nums.count(2)
        for i in range(0,r):
            nums[i]=0
        for i in range(r,r+w):
            nums[i]=1
        for i in range(r+w, len(nums)):
            nums[i]= 2
        return nums
        