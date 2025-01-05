class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue


        
            left = i+1
            right = len(nums)-1
            while left<right:
                t = nums[left]+nums[right]+nums[i]
                if t==target:
                    # if [nums[p], nums[left], nums[right]] not in res:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    # break
                elif t>target:
                    right -=1
                else:
                    left+=1
        return res