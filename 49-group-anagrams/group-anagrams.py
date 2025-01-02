class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= {}
        for i in strs:
            print(''.join(sorted(i)))
            if ''.join(sorted(i)) in d.keys():
                d[''.join(sorted(i))].append(i)
            else:
                d[''.join(sorted(i))]=[i]

        return list(d.values())