class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        nums.sort()
        count = 1
        mx = 1

        i = 0
        while i<len(nums)-1:
            if nums[i+1]-nums[i]==1:
                count +=1
                mx = max(mx, count)
            elif nums[i+1]-nums[i]==0:
                i+=1
                continue
                
            else:
                count = 1
            i+=1
        return mx