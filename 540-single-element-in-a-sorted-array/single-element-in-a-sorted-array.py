class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r = len(nums)-1
        if len(nums)==1: return nums[0]
        if nums[0]!= nums[1]: return nums[0]
        if nums[-1]!= nums[-2]: return nums[-1]
        while l<=r:
            m = (l+r)//2
            mid = nums[m]
            if nums[m-1]!=mid and nums[m+1]!=mid:
                return mid
            elif (mid == nums[m+1] and m%2 ==0) or (nums[m-1]==mid and m%2==1):
                l=m+1
            else: # nums[m+1]==mid:
                r= m-1
        return nums[l]
