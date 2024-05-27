class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # if x>arr[-1]: return arr[len(arr)-k:]
        # if x<arr[0]: return arr[:k]
        # w = arr[0:k]
        # res =[]
        # diff = 20000000
        # for r in range(k, len(arr)):
        #     tdiff = sum([abs(arr[i]-x) for i in w])
        #     print(tdiff)
        #     if tdiff<=diff: res = w
        #     diff = min(diff, tdiff)
        #     print(w)
        #     w = w[1:].append(arr[r])
        #     print(w)
        # return res
        left = 0
        right = len(arr) - 1

        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
  
        return arr[left : right + 1]
        