class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(n):
            if n== 1:
                return ['()']
            pl = dfs(n-1)
            s = []
            for i in pl:
                for j in range(len(i)+1):
                    s.append(i[:j]+'()' + i[j:])
            return list(set(s))
        if n==1:
            return ["()"]
        else:
            return sorted(dfs(n))
