class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {}
        for i, val in enumerate(nums):
            if val in seen and i-seen[val]<=k:
                return True
            else: 
                seen[val] = i
        return False
        # for i in range(len(nums)-k):
        #     if nums[i] == nums[i+k]:
        #         return True
        # return False