class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = [0]*len(nums)
        print(n)
        for i in (nums):
            n[i-1] = 1
        res = []
        for i in range(len(n)):
            if n[i] == 0:
                res.append(i+1)
        return res