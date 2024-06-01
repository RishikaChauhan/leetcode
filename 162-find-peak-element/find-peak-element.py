class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        if len(nums)==2: return nums.index(max(nums[0], nums[1]))
        if nums[0]>nums[1]: return 0
        if nums[-1]>nums[-2]: return len(nums)-1
        # l = 0
        # r = len(nums)-1
        # while l<=r:
        #     m = (l+r)//2
        #     if nums[m-1] <nums[m] and nums[m]>nums[m+1]:
        #         return m
        #     if nums[m-1] <nums[m]: 
        #         l = m+1
        #     else:
        #         r = m-1
        # return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if mid < len(nums) - 1 and nums[mid] < nums[mid+1]:
                l = mid + 1
            elif mid > 0 and nums[mid] < nums[mid-1]:
                r = mid - 1
            else:
                return mid
        # return mid