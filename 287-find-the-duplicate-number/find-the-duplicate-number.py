class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = [0]*len(nums)
        for i in nums:
            if i == l[i]:
                return i
            else:
                l[i] = i
            