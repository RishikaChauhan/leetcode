class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        cz = 0
        if nums.count(0)==1:
            k =nums.index(0) 
            cz = 1
        elif nums.count(0)>1:
            cz = 2

        for i in range(len(nums)):
            if nums[i]==0:
                continue
            else:
                p = p*nums[i]
        
        if cz>1:
            return [0]*len(nums)
        elif cz==1:
            l = [0]*len(nums)
            l[k] = p
            return l
        else:
            return [(lambda x: p // x)(num) for num in nums]

        

# from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         p = 1
#         zero_count = 0
        
#         # Count the number of zeros in the array
#         for num in nums:
#             if num == 0:
#                 zero_count += 1
#             else:
#                 p *= num
        
#         # If more than one zero, all products will be zero
#         if zero_count > 1:
#             return [0] * len(nums)
        
#         result = [0] * len(nums)
        
#         # If there's exactly one zero, set product for that position only
#         if zero_count == 1:
#             zero_index = nums.index(0)
#             result[zero_index] = p
#             return result
        
#         # If there are no zeros, calculate the product for each non-zero position
#         for i in range(len(nums)):
#             result[i] = p // nums[i]

#         return result
