class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d = {}
    
    # Count occurrences of 0, 1, and 2
        for i in nums:
            d[i] = 1 + d.get(i, 0)

        # Ensure missing keys default to 0
        d[0] = d.get(0, 0)
        d[1] = d.get(1, 0)
        d[2] = d.get(2, 0)

        # Overwrite nums in sorted order
        for i in range(d[0]):
            nums[i] = 0
        for j in range(d[0], d[0] + d[1]):
            nums[j] = 1
        for k in range(d[0] + d[1], len(nums)):
            nums[k] = 2

