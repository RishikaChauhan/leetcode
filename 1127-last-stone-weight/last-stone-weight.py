class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1 and stones[0]!=0:
            heapq.heappush(stones, heapq.heappop(stones)-heapq.heappop(stones))
        return -stones[0]