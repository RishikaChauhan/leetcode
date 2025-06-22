class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph  = {}
        def build_graph(edg):
            for edge in edg:
                a, b = edge
                if a not in graph:
                    graph[a] = []
                if b not in graph:
                    graph[b] = []
                graph[a].append(b)
                graph[b].append(a)
            return graph       
        
        
        visit=set()
        # def dfs(node):
        #     if not node: return False
        #     if node in visit: return False
        #     if destination in edges[node]:
        #         return True
        #     for i in edges[node]:
        #         dfs(i)
        #         visit.add(i)
        #     return False


        g = build_graph(edges)
        def dfs(grap, src, dest, visit):
            if src == dest: return True
            if src in visit:
                return False
            visit.add(src)
            for nei in graph[src]:
                if dfs(grap, nei, dest, visit):
                    return True
            return False
        return dfs(g, source, destination, visit)
                