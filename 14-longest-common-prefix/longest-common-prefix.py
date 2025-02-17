class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = strs[0]
        pl = len(p)

        for i in strs[1:]:
            while p != i[:pl]:
                pl -=1
                if pl==0:
                    return ""
                p = p[:pl]
        return p