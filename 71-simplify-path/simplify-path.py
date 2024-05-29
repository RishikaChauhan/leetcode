class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        for i in path.split('/'):
            if i =='.':
                continue
            elif i=='':
                continue
            elif i=='..':
                s = s[:-1]
            else:
                s.append(i)
        return '/'+"/".join(s)
