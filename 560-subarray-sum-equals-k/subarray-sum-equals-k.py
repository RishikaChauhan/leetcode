class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sm = 0
        count = 0
        map = defaultdict(int)
        map[0]=1
        for num in nums:
            sm+=num
            rem=sm-k

            if rem in map:
                count+=map[rem]
            
            map[sm] += 1
        return count
        
        # i=0
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)+1):

                p = nums[i:j]
                # if p==[]: pass
                # print(p)
                if sum(p)==k and p!=[]:
                    res+=1
                    
                # elif sum(p)>k and k:
                #     break
        #     # i=i+1
        return res