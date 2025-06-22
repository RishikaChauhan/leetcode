class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neigh = defaultdict(list)
        for n1, n2 in edges:
            neigh[n1].append(n2)
            neigh[n2].append(n1)
            
        def dfs(node):
            if node ==destination: return True
            if node in seen: return False
            seen.add(node)
            for n in neigh[node]:
                if dfs(n):
                    return True
            return False

        seen = set()
        return dfs(source)