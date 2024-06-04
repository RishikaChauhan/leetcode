class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums = sorted(nums)
        # if target<nums[0] or target>nums[-1]: return -1
        # else:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[l]<=nums[m]:

                if target<=nums[m] and target>=nums[l]:
                    r = m-1
                else:
                    l = m+1
            else:

                if target>=nums[m] and target<=nums[r]:
                    l= m+1
                else:
                    r = m-1
        return -1

        # if target not in nums: return -1
        # else:
        #     return nums.index(target)