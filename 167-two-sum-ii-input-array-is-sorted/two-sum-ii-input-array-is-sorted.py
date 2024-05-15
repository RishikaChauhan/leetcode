class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            p=numbers[i+1:]
            if target-numbers[i] in p:
                return [i+1, p.index(target-numbers[i])+i+2]
