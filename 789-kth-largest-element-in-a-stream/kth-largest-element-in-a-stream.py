class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        index = self.getindex(val)
        self.nums.insert(index, val)
        return self.nums[-self.k]

    def getindex(self, val):
        left, right = 0, len(self.nums)-1
        while left<=right:
            mid =(left+right)//2
            me = self.nums[mid]
            if me == val:
                return mid
            elif me>val:
                right = mid-1
            else:
                left = mid+1
        return left


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)