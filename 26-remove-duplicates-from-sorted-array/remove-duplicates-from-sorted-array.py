class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i =1
        j = 1
        while j<len(nums):
            while j < len(nums) and nums[j] == nums[i-1]:
                j+=1
            # else:
            if j<len(nums):
                nums[i] = nums[j]
                i+=1
                j+=1

            # nums[i] =nums[j]
            # i+=1
        return i