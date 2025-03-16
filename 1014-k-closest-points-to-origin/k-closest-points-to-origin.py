class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # h = {}  # Dictionary to store distances and points
        
        # for i in points:
        #     o = (i[0]**2 + i[1]**2)  # Fixed exponentiation issue
        #     if o in h:  
        #         h[o].append(i)  # Handle duplicate distances properly
        #     else:
        #         h[o] = [i]

        # l = list(h.keys())  # Get list of distances
        # heapq.heapify(l)  # Min-heap based on distances
        # res = []

        # while len(res) < k:
        #     closest_dist = heapq.heappop(l)  # Get the smallest distance
        #     res.extend(h[closest_dist])  # Add all points with this distance

        # return res[:k]
        h = {}
        for i in points:
            o = (i[0]**2 + i[1]**2)
            if o in h:  
                h[o].append(i)  # Handle duplicate distances properly
            else:
                h[o] = [i]

        l = list(h.keys())
        res = []
        heapq.heapify(l)
        while len(res) < k:
            closest_dist = heapq.heappop(l)  # Get the smallest distance
            res.extend(h[closest_dist])  # Add all points with this distance

        return res[:k]
        # for i in range(k):
        #     res.append(h[heapq.heappop(l)])
        # return res
