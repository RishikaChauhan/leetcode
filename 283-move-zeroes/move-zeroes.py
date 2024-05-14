class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = []
        for i in nums:
            if i != 0:
                n.append(i)
        for i in range(len(n)):
            nums[i]= n[i]
        for i in range(len(n),len(nums)):
            nums[i]=0
        return nums