class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = []
        # for i in range(len(temperatures)):
        #     curr = temperatures[i]
        #     j = i+1
        #     while j< (len(temperatures)) and temperatures[j]<=curr:
        #         j+=1
        #     if j==len(temperatures):
        #         res.append(0)
        #     else:
        #         res.append(j-i)
        # return res

        st = []
        res = [0]* len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[i]>temperatures[st[-1]]:
                idx = st.pop()
                res[idx] = i-idx
            st.append(i)
        return res
