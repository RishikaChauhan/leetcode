class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted(lambda x for x in nums: x**2)
        # return sorted( lambda x: x**2 for x in nums)
        # ans = [n*n for n in nums]
        # return sorted(ans)
        ans  = [0]*len(nums)
        s = 0
        e = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[s])>abs(nums[e]):
                ans[i]= nums[s]*nums[s]
                s+=1
            else:
                ans[i] = nums[e]*nums[e]
                e-=1
        return ans
