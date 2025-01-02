class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
	        d[i] = d.get(i, 0)+1
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        print(list(d.keys()))
        return list(d.keys())[:k]
