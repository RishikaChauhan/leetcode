class Solution:
    def threeSum(self, nums: List[int], target = 0) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            t = target-nums[i]
            l =i+1
            r = len(nums)-1
            sm = nums[l]+nums[r]
            
            while l<r:
                sm = nums[l]+nums[r]
                if sm<t:
                    l+=1
                elif sm>t:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:

                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        #     print(res)
        # print(res)
        return res        

