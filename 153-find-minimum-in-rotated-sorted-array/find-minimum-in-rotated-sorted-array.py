class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while l<r:
            m= (l+r)//2
            # if nums[m]<nums[m+1] and nums[m]<nums[m-1]:
            #     return nums[m]
            if nums[m]>=nums[r]:
                l = m+1
            elif nums[m]<nums[r]:
                r = m
        return nums[l]
