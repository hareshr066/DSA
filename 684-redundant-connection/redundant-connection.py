class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # n = len(edges)
        # adj = [[] for _ in range(n + 1)]
        # def dfs(node, par):
        #     if visit[node]:
        #         return True
        #     visit[node] = True
        #     for nei in adj[node]:
        #         if nei == par:
        #             continue
        #         if dfs(nei, node):
        #             return True
        #     return False
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        #     visit = [False] * (n + 1)

        #     if dfs(u, -1):
        #         return [u, v]
        # return []

        # Union find 
        n = len(edges)
        parent = list(range(n+1))
        size = [1]*(n+1)
        def find(x):
            if parent[x]!=x :
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a==root_b:
                return False
            if size[root_a]<size[root_b]:
                root_a,root_b = root_b,root_a
            parent[root_b]=root_a
            size[root_a]+=size[root_b]
            return True
        
        for u,v in edges :
            if not union(u,v):
                return [u,v]
        return []
        