class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        seen = set()
        counter = 0
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        ##dfs will now go through all connected components of a given node.
        for nodeNum in range(n):
            if nodeNum in seen:
                continue
            else:
                dfs(nodeNum)
                counter += 1
        return counter            