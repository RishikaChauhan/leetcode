class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        def search(m):
            to, i = 0, 1
            while i<n:
                if nums[i]-nums[i-1]<=m:
                    to+=1
                    i+=2
                else:
                    i+=1
            return to
        l = 0
        r = nums[-1]-nums[0]
        while l<r:
            m = (l+r)//2
            t= search(m)
            if t<p:
                l= m+1
            else:
                r = m

        return l