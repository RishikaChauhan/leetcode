class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}        
        ans = []
        
        for char in nums:
            counter[char] = counter.get(char, 0)+1

        # for item in counter.items():
        slis = sorted(counter.items(), key = lambda item: item[1], reverse =True)
                # slis = sorted(lis.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            ans.append(slis[i][0])
        return ans
        # ret = []
        # for i in range(len(res)-1, 0, -1):
        #     for j in res[i]:
        #         ret.append(j)
        #         if len(ret)==k:
        #             return ret
        # lis = {} 
        # ans = [] 
        # for x in nums:
        #     if x in lis:
        #         lis[x] += 1
        #     else:
        #         lis[x] = 1
        # print(type(lis.items()))
        # # Step 2: Sort the dictionary items based on frequency in descending order.
        # slis = sorted(lis.items(), key=lambda item: item[1], reverse=True)
        
        # # Step 3: Extract the top k frequent elements and append them to the ans list.
        # for i in range(k):
        #     ans.append(slis[i][0])
        
        # return ans