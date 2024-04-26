class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def isanagram(a:str,b:str):
        #     if len(a)!=len(b):
        #         return False
        #     d={}
        #     for i in a:
        #         d[i]= d.get(i, 0)+1
        #     for i in b:
        #         if i not in d or d[i]==0:
        #             return False
        #         else: d[i]-=1
        #     return True
            
        res ={}
        print(strs[0], "".join(sorted(strs[0])))
        res["".join(sorted(strs[0]))]=[strs[0]]
        print(res)
        for word in strs[1:]:
            k = ''.join(sorted(word))
            if k in list(res.keys()):
                res[k].append(word)
            else:
                res[k]=[word]
        return list(res.values())