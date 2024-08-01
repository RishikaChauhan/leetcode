class Solution:
    def maxScore(self, s: str) -> int:
        # r = 0
        st1 = s[:1]
        st2 = s[1:]
        print(st1, st2)

        ans=  st1.count("0")+st2.count("1")
        print(ans)
        r = ans
        for i in range(1,len(s)-1):
            print(s[i])
            if s[i]=="0":
                # print(ans)
                ans = ans+1
                # print(ans)
            elif s[i]=="1":
                ans = ans-1
            # print(ans)
            r = max(r, ans)
            # ans = max(ans, s[:i].count("0") + s[i:].count("1"))
        return r