class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            n= nums2.index(i)
            count = 0
            for j in range(n+1, len(nums2)):
                count=0
                if nums2[j]>i:
                    res.append(nums2[j])
                    count = 1
                    break
            if count ==0:
                res.append(-1)

        return res