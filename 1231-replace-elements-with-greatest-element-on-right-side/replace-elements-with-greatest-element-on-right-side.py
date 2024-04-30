class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx= temp = arr[-1]
        # res = [0]*len(arr)
        for i in range(len(arr)-2, -1, -1):
            mx = max(mx, temp)
            temp = arr[i]
            arr[i] = mx
        arr[-1] = -1
        return arr
