class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l= 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]== target: return m
            if nums[m]>=nums[l]:
                if nums[m]>=target>=nums[l]:
                    r =m-1
                else:
                    l = m+1
            else:
                if nums[m]<=target<=nums[r]:
                    l=m+1
                else: r=m-1
        return -1