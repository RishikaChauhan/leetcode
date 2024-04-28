class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        flag = 0
        if nums == [0]*len(nums): return nums
        if nums.count(0)>1: return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                prod *=nums[i]
            else:
                flag = 1
                continue
        res = []
        if flag == 1:

            for i in range(len(nums)):
                if nums[i]==0:
                    res.append(prod)
                else:
                    res.append(0)
        else:
            for i in range(len(nums)):
                res.append(prod//nums[i])
        return res