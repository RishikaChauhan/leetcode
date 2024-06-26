class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return True
            if nums[l]>nums[m]:  #right
                if nums[r]>= target>nums[m]:
                    l = m+1
                else:
                    r = m-1
            elif nums[l]<nums[m]:  #left
                if nums[l]<= target<nums[m]:
                    r = m-1
                else:
                    l = m+1
            else: l+=1
            
        return False