class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rg = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            rg1 = max(arr[i],rg) 
            arr[i] = rg
            rg = rg1
        return arr