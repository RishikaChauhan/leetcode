class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= {}
        heap = []
        for i in nums:
            d[i] = 1 + d.get(i,0)
        print(d)

        for o, v in d.items():
            heapq.heappush(heap, (v, o))
        l = heapq.nlargest(k, heap)
        return [i[1] for i in l] 
        