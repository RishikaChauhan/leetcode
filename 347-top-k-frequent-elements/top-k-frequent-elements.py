class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = [[]for i in range(len(nums)+1)]
        # counter = {}        
        
        # for char in nums:
        #     counter[char] = counter.get(char, 0)+1

        # for k,v in counter.items():
        #     res[v].append(k)
        # ret = []
        # for i in range(len(res)-1, 0, -1):
        #     for j in res[i]:
        #         ret.append(j)
        #         if len(ret)==k:
        #             return ret
        lis = {} 
        ans = [] 
        for x in nums:
            if x in lis:
                lis[x] += 1
            else:
                lis[x] = 1
        
        # Step 2: Sort the dictionary items based on frequency in descending order.
        slis = sorted(lis.items(), key=lambda item: item[1], reverse=True)
        
        # Step 3: Extract the top k frequent elements and append them to the ans list.
        for i in range(k):
            ans.append(slis[i][0])
        
        return ans