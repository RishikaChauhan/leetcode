class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mn =nums[-1]
        if len(nums)==1: return 0
        for i in range(len(nums)-k+1):
            mn= min(mn, nums[k+i-1]-nums[i])
        return mn