class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right = len(numbers)-1
        while left<right:
            total = numbers[left]+numbers[right]
            if total== target: return [left+1,right+1]
            elif total>target:
                right= right-1
            else: left = left+1
        
        
        
        
        
        
        
        for i in range(len(numbers)):
            p=numbers[i+1:]
            if target-numbers[i] in p:
                return [i+1, p.index(target-numbers[i])+i+2]
