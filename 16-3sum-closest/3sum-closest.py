class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        def ksumclosest(nums, k, target):
            n = len(nums)
            if n==k:
                return sum(nums[:k])

            current = (sum(nums[:k]))
            if current>= target:
                return current
            current = sum(nums[-k:])
            if current<= target:
                return current
            if k == 1:
                return min([(x, abs(target-x)) for x in nums], key = lambda x:x[1])[0]
            closest = sum(nums[:k])
            for i, x in enumerate(nums[:-k+1]):
                if i>0 and x==nums[i-1]:
                    continue
                current = ksumclosest(nums[i+1:],k-1, target-x)+x
                if abs(target-current)<abs(target-closest):
                    if current == target:
                        return target
                    else: closest = current
            return closest

        return ksumclosest(nums, 3, target)
        
        
        ans = sum(nums[:3])

        if nums[0]+nums[1]+nums[2]>=target:
            return nums[0]+nums[1]+nums[2]
        
        if nums[-1]+nums[-2]+nums[-3]<=target:
            return nums[-1]+nums[-2]+nums[-3]
        
        dif= mn= abs(ans-target)
        for i in range(3, len(nums)):
            ans = ans + nums[i]-nums[i-3]
            dif = abs(ans-target)
            if dif == 0:
                return ans
            if dif<mn:
                mn = dif
            else:
                return ans +nums[i-3]-nums[i]    
        