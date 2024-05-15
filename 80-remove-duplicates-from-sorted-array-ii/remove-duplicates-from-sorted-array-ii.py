class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p=1
        for i in range(1, len(nums)):
            if  p==1 or nums[i]!= nums[p-2]:
                nums[p]=nums[i]
                p+=1
        return p