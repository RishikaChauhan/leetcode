class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        # arr.sort()
        count =0
        sub = arr[0:k] 
        sm = sum(sub)
        if sum(sub)//k>=t: count +=1
        for i in range(len(arr)-k):
            sm += arr[i+k]-arr[i]
            if sm//k>= t:
                # print(sum(sub))
                count+=1
        return count