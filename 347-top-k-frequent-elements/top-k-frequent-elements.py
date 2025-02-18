class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= {}
        # heap = []
        for i in nums:
            d[i] = 1 + d.get(i,0)
        # print(d)

        # for o, v in d.items():
        #     heapq.heappush(heap, (v, o))
        # l = heapq.nlargest(k, d.items(), key = lambda x: x[1])
        top_k = heapq.nlargest(k, d.items(), key=lambda x: x[1])
        return [i[0] for i in top_k] 
        