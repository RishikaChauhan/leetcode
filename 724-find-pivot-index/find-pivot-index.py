class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsm = sum(nums)-nums[0]
        lsm = 0
        if lsm==rsm: return 0
        for i in range(1, len(nums)):
            lsm+=nums[i-1]
            rsm-=nums[i]
            if lsm==rsm: return i
        
        return -1