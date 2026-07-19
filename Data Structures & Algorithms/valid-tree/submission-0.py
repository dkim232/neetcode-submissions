class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #valid tree: has no cycles
        tree = defaultdict(list)
        for r1,r2 in edges:
            tree[r1].append(r2)
            tree[r2].append(r1)
        
        seen = set()
        def dfs(node, prev):
            if node in seen:#cycle detection
                return False

            #so node is not seen before, and isn't equal to prev.
            seen.add(node)
            for neighbor in tree[node]:
                if neighbor == prev: #would be backing up; skip
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0,-1):
            return False
        return len(seen) == n