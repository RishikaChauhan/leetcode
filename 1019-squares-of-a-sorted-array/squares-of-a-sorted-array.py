class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted(lambda x for x in nums: x**2)
        # return sorted( lambda x: x**2 for x in nums)
        ans = [n*n for n in nums]
        return sorted(ans)