class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if set(nums1)=={0}:
            for i in range(len(nums1)):
                nums1[i]=nums2[i]

        if nums2==[]: return nums1
        p1 = m+n-1
        # while p1>0:
        m1= m-1
        n1 = n-1
        while n1>=0:
            print(p1, m1, n1)
            if nums1[m1]>nums2[n1] and m1 >=0:
                
                nums1[p1]=nums1[m1]
                # nums1[m1]= nums2[n1]
                m1 = m1-1
            else:
                nums1[p1]=nums2[n1]
                # nums2[n1] = nums1[m1]
                n1 = n1-1
            p1 = p1-1
        return nums1
