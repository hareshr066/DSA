class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        visited=[False]*len(graph)
        pathvis = [False]*len(graph)
        check = [0]*len(graph)
        def dfs(node):
            visited[node]=True
            pathvis[node]=True
            check[node]=0
            for nei in graph[node]:
                #not visited
                if not visited[nei]:
                    if dfs(nei):
                        return True
                # not visited
                elif pathvis[nei]:
                    return True
            pathvis[node]=False
            check[node]=1
        for i in range(len(graph)):
            if not visited[i]:
                dfs(i)
        safe = []
        for i in range(len(check)):
            if check[i]==1 :
                safe.append(i)
        return safe
        

        