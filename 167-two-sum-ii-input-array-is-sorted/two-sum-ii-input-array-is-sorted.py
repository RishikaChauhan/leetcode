class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        sm = numbers[l] + numbers[r]
        while l<r:
            if sm>target:
                r = r-1
            elif sm<target:
                l= l+1
            else:
                return [l+1,r+1]
            sm = numbers[l] + numbers[r]