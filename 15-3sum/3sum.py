class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triplet = [nums[i], nums[l], nums[r]]
                    answer.append(triplet)
                    while l < r and nums[l] == triplet[1]:
                        l += 1
                    while l < r and nums[r] == triplet[2]:
                        r -= 1
        return answer
        res = []
        nums.sort()
        target=0
        # ilist=[]
        for i in range(len(nums)):
            if nums[i] ==nums[i-1] and i!=0:
                continue
            else:
                # ilist.append(nums[i])
                left=i+1
                right = len(nums)-1
                while left<right:
                    if nums[left]==nums[left-1] and left==i+2:
                        left=left+1
                        continue
                    elif right ==len(nums)-2 and nums[right]==nums[right+1]:
                        right=right-1
                        continue
                    else:
                        total = nums[left]+nums[right]+nums[i]
                        if total== target and [nums[i],nums[left],nums[right]] not in res: 
                            res.append([nums[i],nums[left],nums[right]])
                            left+=1
                            # break
                        elif total>target:
                            right= right-1
                        else: left = left+1
                    
        return res