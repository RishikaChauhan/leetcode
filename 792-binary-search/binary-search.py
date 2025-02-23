class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if 
        l = 0
        r = len(nums)-1
        
        while l<=r:
            m = (l+r)//2
            if nums[m]>target:
                r = m-1
            elif nums[m]<target:
                l = m+1
            else:
                return m
            # m = (l+r)//2
        return -1