class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        c = 0
        for i in range(len(nums)):
            if nums[i]!= 0:
                p = p*nums[i]
            else:
                c +=1
        res = []
        if c==0:
            for i in range(len(nums)):
                res.append(p//nums[i])
            return res
        elif c==1:
            res = [0]*len(nums)
            for i in range(len(nums)):
                if nums[i]==0:
                    res[i] = p
            return res
        else:
            return [0]*len(nums)