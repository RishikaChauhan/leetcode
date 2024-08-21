class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        mx = nums[-1]
        nums[-1] = -1
        for i in range(len(nums)-2,-1,-1):
            temp =nums[i]
            nums[i] = mx
            mx = max(mx, temp)
            
        return nums