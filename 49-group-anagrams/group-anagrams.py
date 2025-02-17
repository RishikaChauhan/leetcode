class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            if "".join(sorted(i)) in d:
                d["".join(sorted(i))].append(i)
            else:
                d["".join(sorted(i))] = [i]
        print(d)
        return list(d.values())
        
        
        
        
        
        
        # d ={}
        # for i in strs:
        #     d["".join(sorted(i))] = 1 + d.get(i,0)
        # print(d)
        # return list(d.values())