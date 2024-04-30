class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        res = [0]*len(arr)
        for i in range(len(arr)-2, -1, -1):
            mx = max(mx, arr[i+1])
            res[i] = mx
        res[-1] = -1
        return res
