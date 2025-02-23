class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l= 0
        # r = len(nums)-1
        # while l<=r:
        #     m = (l+r)//2
        #     if nums[m]>nums[l]:
        #         l = m+1
        #     elif nums[m]<nums[l]:
        #         r =m-1
        #     elif nums[m]<nums[r]:
        #         r = m-1
        #     elif nums[m]>nums[r]:
        #         l = m+1
        # return nums[l]

        l = 0
        r = len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m+1
        return nums[l]