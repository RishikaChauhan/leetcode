class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for x,y in edges:
            tree[x].append(y)
            tree[y].append(x)

        def dfs(root, parent = None):
            cost = 0
           
            for child in tree[root]:
                if child != parent:
                    cost += dfs(child, root)

# Check if any of the child contains Apple or node itself has apple. 
            if root != 0 and (cost > 0 or hasApple[root]):
                return cost + 2
           
            return cost

        return dfs(0)