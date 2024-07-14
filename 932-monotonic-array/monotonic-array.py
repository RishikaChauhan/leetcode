class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0]<nums[-1]:
            for i in range(1, len(nums)):
                if nums[i]<nums[i-1]:
                    return False
        elif nums[0]>nums[-1]:
            for i in range(1, len(nums)):
                if nums[i]>nums[i-1]:
                    return False
        else:
            for i in range(1, len(nums)-1):
                if nums[i]!=nums[i-1]:
                    return False
            # if nums[i+1]>nums[i]<nums[i-1] or nums[i+1]<nums[i]>nums[i-1]:
            #     return False
        
        return True
