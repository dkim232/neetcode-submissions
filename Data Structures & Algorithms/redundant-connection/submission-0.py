class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #union find
        parent = [i for i in range(len(edges)+1)]

        def find(node):
            #find the parent of a node
            if parent[node] == node:#found parent
                return node
            else:# not the parent yet
                parent[node]=find(parent[node])
                return parent[node]

        def union(a,b):#take 2 inputs and make 1
            a_parent = find(a)
            b_parent = find(b)
            
            parent[a_parent] = b_parent
            
        
        for a,b in edges:
            if find(a) == find(b):
                return [a,b]
            else:
                union(a,b)
            