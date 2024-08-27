class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =[]
        d = {}
        for i in strs:
            a = "".join(sorted(i))
            if a in list(d.keys()):
                d[a].append(i)       
            else:
                d[a]=[i]
        return list(d.values())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = []
        # d = {}
        # for i in strs:
        #     a = "".join(sorted(i))
        #     if a in list(d.keys()):
        #         d[a].append(i)
        #     else:
        #         d[a]=[i]
        # return list(d.values())