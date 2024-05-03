class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def num_mapp(s):           
            indx = []
            res = ''
            for i in s:
                if i in indx:
                    res+=str(indx.index(i)+1)
                else:
                    indx.append(i)
                    res+=str(len(indx))
            return res
        return num_mapp(s)==num_mapp(t)
                
